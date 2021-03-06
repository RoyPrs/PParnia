# Generated by Django 3.2.3 on 2021-09-14 11:47

import common.model_mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_id', models.CharField(max_length=20, unique=True, verbose_name='Complain ID')),
                ('text', models.TextField(max_length=300, verbose_name='Complain Text')),
                ('status', models.CharField(choices=[('Seen', 'Seen'), ('Unseen', 'Unseen')], default='Unseen', max_length=10, verbose_name='Seen or not')),
            ],
            options={
                'verbose_name': 'Complain',
                'verbose_name_plural': 'Complains',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, help_text='Public ID to identify an individual course.', max_length=30, unique=True, verbose_name='Public Course ID')),
                ('name', models.CharField(help_text='The name of the course', max_length=50, unique=True, verbose_name='Course Name')),
                ('credit', models.PositiveSmallIntegerField(help_text='The credit of the course', verbose_name='Course Credit')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('name',),
            },
            bases=(common.model_mixins.ValidateOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CourseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(max_length=20, unique=True, verbose_name='Course Log ID')),
                ('midterm', models.PositiveSmallIntegerField(blank=True, verbose_name='Midterm Exam Grade')),
                ('final', models.PositiveSmallIntegerField(blank=True, verbose_name='Final Exam Grade')),
                ('final_grade', models.PositiveSmallIntegerField(blank=True, verbose_name='Final Grade')),
                ('status', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Not Approved', 'Not Approved'), ('Approved', 'Approved')], default='Unavailable', max_length=20, verbose_name='Course Status')),
            ],
            options={
                'verbose_name': 'Course Log',
                'verbose_name_plural': 'Course Logs',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, help_text='Public ID to identify an individual term.', max_length=30, unique=True, verbose_name='Public Term ID')),
                ('term', models.CharField(choices=[(1, 'SPRING'), (2, 'SUMMER'), (3, 'FALL'), (4, 'WINTER')], help_text='Term Season', max_length=30, verbose_name='Term')),
                ('start_date', models.DateField(blank=True, help_text='The day on which the term starts.', max_length=4, verbose_name='Term Start Date')),
            ],
            options={
                'verbose_name': 'Term',
                'verbose_name_plural': 'Terms',
                'ordering': ('start_date',),
            },
            bases=(common.model_mixins.ValidateOnSaveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CourseSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(blank=True, help_text='Public ID to identify an individual course.', max_length=30, unique=True, verbose_name='Public Course Section ID')),
                ('local_id', models.PositiveSmallIntegerField(help_text='The identity of the course section among all sections of a course in a term.', verbose_name='Course Section Group')),
                ('total_capacity', models.PositiveSmallIntegerField(help_text='Total Capacity of this Section', verbose_name='Total Capacity')),
                ('first_session_weekday', models.CharField(choices=[('Monday', 'Monday'), ('Tueseday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], help_text='The weekday of the first session.', max_length=30, verbose_name='First Session Weekday')),
                ('second_session_weekday', models.CharField(choices=[('Monday', 'Monday'), ('Tueseday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], help_text='The weekday of the second session.', max_length=30, verbose_name='Second Session Weekday')),
                ('hour_schedule', models.CharField(choices=[('8-10', '8-10'), ('10-12', '10-12'), ('2-4', '2-4'), ('4-6', '4-6'), ('6-8', '6-8')], help_text='Hours of the class', max_length=30, verbose_name='Hour of the Class')),
                ('exam_date', models.DateField(help_text='The date and time of the exam', max_length=30, verbose_name='Exam Date')),
                ('course', models.ForeignKey(help_text='The course for which this section is defined.', on_delete=django.db.models.deletion.CASCADE, to='course_management.course', verbose_name='Corresponding Course')),
            ],
            options={
                'verbose_name': 'Course Section',
                'verbose_name_plural': 'Course Sections',
                'ordering': ('course__name',),
            },
            bases=(common.model_mixins.ValidateOnSaveMixin, models.Model),
        ),
    ]
