# Generated by Django 3.2.3 on 2021-09-14 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesection',
            name='instructor',
            field=models.ForeignKey(help_text='The instructor if the class', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Instructor'),
        ),
        migrations.AddField(
            model_name='coursesection',
            name='term',
            field=models.ForeignKey(help_text='The term in which this class section is held.', on_delete=django.db.models.deletion.CASCADE, to='course_management.term', verbose_name='Term'),
        ),
        migrations.AddField(
            model_name='courselog',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_management.coursesection', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='courselog',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='prerequesits',
            field=models.ManyToManyField(blank=True, help_text='The courses one must pass before taking this course.', to='course_management.Course', verbose_name='Prerequesit Courses'),
        ),
        migrations.AddField(
            model_name='complain',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_management.coursesection'),
        ),
        migrations.AddField(
            model_name='complain',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='complain',
            unique_together={('student', 'section')},
        ),
    ]
