# Generated by Django 3.2.3 on 2021-10-14 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_management', '0012_alter_courselog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesection',
            name='course',
            field=models.ForeignKey(help_text='The course for which this section is defined.', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='course_management.course', verbose_name='Corresponding Course'),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='instructor',
            field=models.ForeignKey(help_text='The instructor of the class', on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL, verbose_name='Instructor'),
        ),
        migrations.AlterField(
            model_name='coursesection',
            name='term',
            field=models.ForeignKey(help_text='The term in which this class section is held.', on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='course_management.term', verbose_name='Term'),
        ),
    ]
