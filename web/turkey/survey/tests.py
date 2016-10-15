import json

import time
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ValidationError
from django.test import Client
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from selenium import webdriver

from web.turkey.survey import default_settings
from .models import Task, Token, TaskInteraction, StepTextInput, AuditorClicksTotal, AuditorClicksTotalData


class AbstractTestCase(TestCase):
    TASK_IS_EXTERNAL = False
    TASK_IS_PUBLISHED = True

    def setUp(self):
        self.admin_user = User.objects.create_user('admin', 'admin@admin.com', 'adminpassword')
        self.internal_task = Task(survey_name='Bestest Task',
                                  external=self.TASK_IS_EXTERNAL,
                                  published=self.TASK_IS_PUBLISHED)
        self.internal_task.save()
        self.internal_task.owners.add(self.admin_user)
        self.token = Token.objects.create()
        self.client = Client()


class BasicAuditorSubmissionTestCase(AbstractTestCase):
    SUBMISSION_OBJECTS_KEY = 'auditors'

    def create_task_interaction(self):
        return TaskInteraction.objects.create(task=self.internal_task,
                                              token=self.token)

    def post_basic_submission(self, interaction):
        return self.post_json_submission(interaction,
                                         {'token': self.token.token.decode(),
                                          self.SUBMISSION_OBJECTS_KEY: {}})

    def post_json_submission(self, interaction, data):
        return self.client.post(reverse('survey:auditor_submission',
                                        kwargs={'pk': interaction.task.pk}),
                                content_type='application/json',
                                data=json.dumps(data))

    def test_cant_submit_to_unpublished_task(self):
        self.internal_task.published = False
        self.internal_task.save()
        response = self.post_basic_submission(self.create_task_interaction())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_submit_to_published_task(self):
        response = self.post_basic_submission(self.create_task_interaction())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cant_double_submit(self):
        AuditorClicksTotal.objects.create(task=self.internal_task)
        interaction = self.create_task_interaction()
        response = self.post_json_submission(
            interaction,
            {
                'token': self.token.token.decode(),
                self.SUBMISSION_OBJECTS_KEY: {
                    'clicks_total': {
                        'count': 5
                    }
                }
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.post_json_submission(
            interaction,
            {
                'token': self.token.token.decode(),
                self.SUBMISSION_OBJECTS_KEY: {
                    'clicks_total': {
                        'count': 5
                    }
                }
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_auditor_submission_serialized(self):
        """
        Test with one of the basic auditors that things are properly going to the database.
        """
        auditor = AuditorClicksTotal.objects.create(task=self.internal_task)
        interaction = self.create_task_interaction()
        self.post_json_submission(
            interaction,
            {
                'token': self.token.token.decode(),
                self.SUBMISSION_OBJECTS_KEY: {
                    'clicks_total': {
                        'count': 5
                    }
                }
            }
        )
        data = AuditorClicksTotalData.objects.filter(general_model=auditor)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].count, 5)

    def test_junk_data_returns_bad_request(self):
        AuditorClicksTotal.objects.create(task=self.internal_task)
        interaction = self.create_task_interaction()
        response = self.post_json_submission(
            interaction,
            {
                'token': self.token.token.decode(),
                self.SUBMISSION_OBJECTS_KEY: {
                    'clicks_total': {
                        'count': 'fish'
                    }
                }
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenSanityChecks(AbstractTestCase):
    def test_can_create(self):
        Token.objects.create()


class TaskSanityChecks(AbstractTestCase):
    def test_can_modify_without_submission(self):
        self.internal_task.survey_name = 'Worstest Task'
        self.internal_task.full_clean()
        self.internal_task.save()

    def test_cant_change_test_to_external_without_deleting_steps(self):
        step = StepTextInput.objects.create(task=self.internal_task,
                                            title='Are you truly happy',
                                            text='If you lie you\'re only '
                                                 'hurting yourself',
                                            step_num=1)
        self.internal_task.external = True
        with self.assertRaises(ValidationError):
            self.internal_task.full_clean()
        step.delete()
        self.internal_task.full_clean()

    def invalid_task_modification(self, modification_function):
        TaskInteraction.objects.create(token=self.token,
                                       task=self.internal_task)
        modification_function(self.internal_task)
        with self.assertRaises(ValidationError):
            self.internal_task.full_clean()

    def test_cant_make_unnamed_internal_task(self):
        task = Task(survey_name='', external=False)
        with self.assertRaises(ValidationError):
            task.full_clean()

    def test_cant_modify_name_after_submission(self):
        """
        Tests whether we are keeping users from modifying tasks after
        users have already submitted responses, or auditors have already
        collected data. This protects data consistency on our end.

        Any user interaction is represented by a task interaction.
        """

        def mod(task):
            task.survey_name = 'Worstest'

        self.invalid_task_modification(mod)

    def test_cant_modify_external_status_after_submission(self):
        def mod(task):
            task.external = True

        self.invalid_task_modification(mod)


class AuditorTotalClicksTestCase(StaticLiveServerTestCase):
    def setUp(self):
        super().setUpClass()
        self.selenium = webdriver.Chrome('/usr/local/bin/chromedriver')
        self.token = Token.objects.create()
        self.task = Task(survey_name='Bestest Task',
                         external=False,
                         published=False)
        self.selenium.get(self.get_url('admin:login'))
        self.selenium.add_cookie({
            'name': default_settings.SURVEY_CONFIG['TOKEN_NAME'],
            'value': self.token.token.decode(),
            'path': '/',
            'domain': self.server_thread.host
        })
        self.task.save()
        self.clicks_auditor = AuditorClicksTotal.objects \
            .create(task=self.task)
        self.task.published = True
        self.task.save()

    def get_url(self, name, kwargs=None):
        return self.live_server_url + reverse(name, kwargs=kwargs)

    def test_clicks_recorded(self):
        NUMBER_CLICKS = 3
        self.selenium.get(self.get_url('survey:TaskPage',
                                       kwargs={'pk': self.task.pk}))
        body = self.selenium.find_element_by_tag_name('body')
        for _ in range(NUMBER_CLICKS):
            body.click()
        self.selenium.find_element_by_id('submit').click()
        interaction = TaskInteraction.objects.filter(task=self.task)
        self.assertEqual(len(interaction), 1)
        interaction = interaction[0]
        auditor_data = AuditorClicksTotalData.objects.filter(task_interaction_model=interaction)
        time.sleep(1)
        self.assertEqual(len(auditor_data), 1)
        auditor_data = auditor_data[0]
        # add one for submission button click
        self.assertEqual(auditor_data.count, NUMBER_CLICKS + 1)
