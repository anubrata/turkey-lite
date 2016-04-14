# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 20:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditorBeforeTypingDelay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Before Typing Delay Auditor',
                'verbose_name_plural': 'Before Typing Delay Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorClicksSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Clicks Specific Auditor',
                'verbose_name_plural': 'Clicks Specific Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorClicksTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Clicks Total Auditor',
                'verbose_name_plural': 'Clicks Total Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorFocusChanges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Focus Changes Auditor',
                'verbose_name_plural': 'Focus Changes Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorKeypressesSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Keypresses Specific Auditor',
                'verbose_name_plural': 'Keypresses Specific Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorKeypressesTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Keypresses Total Auditor',
                'verbose_name_plural': 'Keypresses Total Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorMouseMovementSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Mouse Movement Specific Auditor',
                'verbose_name_plural': 'Mouse Movement Specific Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorMouseMovementTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Mouse Movement Total Auditor',
                'verbose_name_plural': 'Mouse Movement Total Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorOnFocusTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'On Focus Time Auditor',
                'verbose_name_plural': 'On Focus Time Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorPastesSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Pastes Specific Auditor',
                'verbose_name_plural': 'Pastes Specific Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorPastesTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Pastes Total Auditor',
                'verbose_name_plural': 'Pastes Total Auditors',
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorRecordedTimeDisparity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Recorded Time Disparity Auditor',
                'verbose_name_plural': 'Recorded Time Disparity Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorScrolledPixelsSpecific',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Scrolled Pixels Specific Auditor',
                'verbose_name_plural': 'Scrolled Pixels Specific Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorScrolledPixelsTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Scrolled Pixels Total Auditor',
                'verbose_name_plural': 'Scrolled Pixels Total Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorTotalTaskTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Total Task Time Auditor',
                'verbose_name_plural': 'Total Task Time Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuditorWithinTypingDelay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Within Typing Delay Auditor',
                'verbose_name_plural': 'Within Typing Delay Auditors',
                'ordering': ['task', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepMultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('step_num', models.IntegerField(help_text='Controls the order that steps linked to a task are to be taken in by the user', verbose_name='Step Number')),
                ('title', models.CharField(help_text='Title for multiple choice prompt. Choose carefully. This and associated responses are not allowed to change after the first user has responded to this multiple choice step. Then, you must create a new Multiple Choice Step', max_length=144, verbose_name='Title')),
                ('text', models.TextField(help_text='The text to go along with your multiple choice prompt. Choose carefully. This and associated responses are not allowed to change after the first user has responded to this multiple choice step. Then, you must create a new Multiple Choice Step', verbose_name='Multiple Choice Text')),
                ('randomize_order', models.BooleanField(default=False, help_text='Randomizes the order in which responses are presented to the user under a Multiple Choice Step if selected', verbose_name='Randomize Response Order')),
            ],
            options={
                'verbose_name': 'Multiple Choice Step',
                'verbose_name_plural': 'Steps',
                'ordering': ['task', 'step_num', '-updated', '-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepMultipleChoiceResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('text', models.TextField(help_text='Text for one of the responses to a Multiple Choice Step', verbose_name='Multiple Choice Response Text')),
                ('order', models.IntegerField(blank=True, help_text='Controls the order that responses linked to a Multiple Choice Step are to be rendered. The field can be left blank but this only really makes sense if you randomize order of responses in the Multiple Choice Step', null=True, verbose_name='Response Number')),
                ('multiple_choice_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.StepMultipleChoice', verbose_name='Associated Multiple Choice Step for Response')),
            ],
            options={
                'verbose_name': 'Multiple Choice Step Response',
                'verbose_name_plural': 'Steps',
                'ordering': ['order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('survey_name', models.CharField(help_text="This is exposed to the user: Name of the survey they're taking", max_length=144, verbose_name='Survey Name')),
                ('owners', models.ManyToManyField(help_text='Users with permission to view and modify', to=settings.AUTH_USER_MODEL, verbose_name='Owners')),
            ],
            options={
                'verbose_name': 'Interactive Task',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='TaskInteraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('completed', models.BooleanField(default=False)),
                ('task', models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task')),
            ],
            options={
                'verbose_name': 'Task Interaction',
            },
        ),
        migrations.CreateModel(
            name='AuditorBeforeTypingDelayData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('milliseconds', models.IntegerField(blank=True, help_text='total time in milliseconds that the user took before typing', null=True, verbose_name='before typing delay')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorClicksSpecificData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('dom_type', models.TextField(help_text='DOM type of element that was clicked', verbose_name='clicks specific type')),
                ('dom_id', models.TextField(blank=True, help_text='DOM ID of element that was clicked', null=True, verbose_name='clicks specific id')),
                ('dom_class', models.TextField(blank=True, help_text='DOM class of element that was clicked', null=True, verbose_name='clicks specific id')),
                ('dom_name', models.TextField(blank=True, help_text='DOM name of element that was clicked', null=True, verbose_name='clicks specific id')),
                ('time', models.IntegerField(help_text='timestamp of this click event', verbose_name='clicks specific timestamp')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorClicksTotalData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('count', models.IntegerField(help_text='total number of times a user clicked', verbose_name='clicks total')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorFocusChangesData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('time', models.IntegerField(help_text='timestamps of whenever the user switches out of focus', verbose_name='focus changes times')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorKeypressesSpecificData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('key', models.TextField(help_text='specific keys pressed by the user', verbose_name='keypresses specific')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorKeypressesTotalData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('count', models.IntegerField(help_text='total number of times a user pressed a key', verbose_name='keypresses total')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorMouseMovementSpecificData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('x', models.IntegerField(help_text='ending x coordinate of mouse whenever user moves mouse', verbose_name='mouse movement x coordinate')),
                ('y', models.IntegerField(help_text='ending y coordinate of mouse whenever user moves mouse', verbose_name='mouse movement y coordinate')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorMouseMovementTotalData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('amount', models.IntegerField(help_text='total number of pixels traversed by the cursor due to user moving mouse', verbose_name='mouse movement total')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorOnFocusTimeData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('milliseconds', models.IntegerField(help_text='total time in milliseconds that the user spent on focus', verbose_name='on focus time')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorPastesSpecificData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('data', models.TextField(help_text='specific content pasted by the user', verbose_name='pastes specific')),
                ('time', models.IntegerField(help_text='timestamp of this paste event', verbose_name='pastes specific timestamp')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorPastesTotalData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('count', models.IntegerField(help_text='number of times a user pastes something (^V)', verbose_name='pastes total')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorRecordedTimeDisparityData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('milliseconds', models.IntegerField(help_text='total time in milliseconds that the user spent off focus', verbose_name='recorded time disparity')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorScrolledPixelsSpecificData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('horizontal_position', models.IntegerField(help_text='horizontal position on page after scrolling', verbose_name='horizontal scrolled pixels position')),
                ('horizontal_change', models.IntegerField(help_text='horizontal change in position on page after scrolling', verbose_name='horizontal scrolled pixels change')),
                ('vertical_position', models.IntegerField(help_text='vertical position on page after scrolling', verbose_name='vertical scrolled pixels position')),
                ('vertical_change', models.IntegerField(help_text='vertical change in position on page after scrolling', verbose_name='vertical scrolled pixels change')),
                ('time', models.IntegerField(help_text='timestamp of this scroll event', verbose_name='scrolled pixels specific timestamp')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorScrolledPixelsTotalData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('horizontal', models.IntegerField(help_text='total number of pixels scrolled horizontally by the user', verbose_name='scrolled horizontal pixels total')),
                ('vertical', models.IntegerField(help_text='total number of pixels scrolled vertically by the user', verbose_name='scrolled vertical pixels total')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorTotalTaskTimeData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('milliseconds', models.IntegerField(help_text='total time in milliseconds that the user spent on the task page', verbose_name='total task time')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='AuditorWithinTypingDelayData',
            fields=[
                ('auditordata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.AuditorData')),
                ('within_delay', models.TextField(blank=True, help_text='whether the user typed within the delay period', null=True, verbose_name='within typing delay')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.auditordata',),
        ),
        migrations.CreateModel(
            name='StepMultipleChoiceData',
            fields=[
                ('stepdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey.StepData')),
            ],
            options={
                'ordering': ['-updated', '-created'],
                'abstract': False,
            },
            bases=('survey.stepdata',),
        ),
        migrations.AddField(
            model_name='stepmultiplechoice',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='stepdata',
            name='task_interaction_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.TaskInteraction'),
        ),
        migrations.AddField(
            model_name='auditorwithintypingdelay',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditortotaltasktime',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorscrolledpixelstotal',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorscrolledpixelsspecific',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorrecordedtimedisparity',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorpastestotal',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorpastesspecific',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditoronfocustime',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditormousemovementtotal',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditormousemovementspecific',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorkeypressestotal',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorkeypressesspecific',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorfocuschanges',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditordata',
            name='task_interaction_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.TaskInteraction'),
        ),
        migrations.AddField(
            model_name='auditorclickstotal',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorclicksspecific',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='auditorbeforetypingdelay',
            name='task',
            field=models.ForeignKey(help_text='Task that this is linked to', on_delete=django.db.models.deletion.CASCADE, to='survey.Task', verbose_name='Associated Task'),
        ),
        migrations.AddField(
            model_name='stepmultiplechoicedata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.StepMultipleChoice'),
        ),
        migrations.AddField(
            model_name='stepmultiplechoicedata',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.StepMultipleChoiceResponse'),
        ),
        migrations.AddField(
            model_name='auditorwithintypingdelaydata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorWithinTypingDelay'),
        ),
        migrations.AddField(
            model_name='auditortotaltasktimedata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorTotalTaskTime'),
        ),
        migrations.AddField(
            model_name='auditorscrolledpixelstotaldata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorScrolledPixelsTotal'),
        ),
        migrations.AddField(
            model_name='auditorscrolledpixelsspecificdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorScrolledPixelsSpecific'),
        ),
        migrations.AddField(
            model_name='auditorrecordedtimedisparitydata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorRecordedTimeDisparity'),
        ),
        migrations.AddField(
            model_name='auditorpastestotaldata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorPastesTotal'),
        ),
        migrations.AddField(
            model_name='auditorpastesspecificdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorPastesSpecific'),
        ),
        migrations.AddField(
            model_name='auditoronfocustimedata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorOnFocusTime'),
        ),
        migrations.AddField(
            model_name='auditormousemovementtotaldata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorMouseMovementTotal'),
        ),
        migrations.AddField(
            model_name='auditormousemovementspecificdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorMouseMovementSpecific'),
        ),
        migrations.AddField(
            model_name='auditorkeypressestotaldata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorKeypressesTotal'),
        ),
        migrations.AddField(
            model_name='auditorkeypressesspecificdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorKeypressesSpecific'),
        ),
        migrations.AddField(
            model_name='auditorfocuschangesdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorFocusChanges'),
        ),
        migrations.AddField(
            model_name='auditorclickstotaldata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorClicksTotal'),
        ),
        migrations.AddField(
            model_name='auditorclicksspecificdata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorClicksSpecific'),
        ),
        migrations.AddField(
            model_name='auditorbeforetypingdelaydata',
            name='general_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.AuditorBeforeTypingDelay'),
        ),
    ]
