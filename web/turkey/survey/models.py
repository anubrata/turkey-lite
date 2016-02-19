from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from .steps import *  # we have to get all the user defined models from steps
from .auditors import *  # we have to get all the user defined models from auditors


# Create your models here.
class Task(models.Model):
    number_simultaneous_users = models.IntegerField(
        verbose_name=_('Number of simultaneous users'),
        help_text=_('Number of users who need to be in the lobby and ready '
                    'to begin before they may start the task')
    )
    task_dependencies = models.ManyToManyField(
        'Task',
        verbose_name=_('Task Dependencies'),
        help_text=_('Tasks that must be completed before this task by a given user')
    )
    survey_wrap_template = 'survey/survey_default_template.html'
    lobby_template = 'survey/lobby_default_template.html'
    auditors = models.ManyToManyField(
        'Auditor',
        verbose_name=_('Auditors'),
        help_text=_('Auditors attached to this task\'s main page')
    )
    owners = models.ManyToManyField(
        User,
        verbose_name=_('Owners'),
        help_text=_('Users with permission to view and modify')
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Interactive Task')
        ordering = ['-updated']


class Step(models.Model):
    task = models.ForeignKey(
        'Task',
        verbose_name=_('Associated Task'),
        help_text=_('Task that this step is linked to')
    )
    step_num = models.IntegerField(
        verbose_name=_('Step Number'),
        help_text=_('Controls the order that steps linked to a task are to be '
                    'taken in by the user')
    )
    # template_code = 'survey/my_step_template.html'

    class Meta:
        abstract = True
        ordering = ['task', 'step_num', '-updated']


class Auditor(models.Model):
    task = models.ForeignKey(
        'Task',
        verbose_name=_('Associated Task'),
        help_text=_('Task that this step is linked to')
    )
    # template_code = 'survey/my_auditor_template.html

    class Meta:
        abstract = True
