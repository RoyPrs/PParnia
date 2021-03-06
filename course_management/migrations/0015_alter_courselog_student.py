# Generated by Django 3.2.3 on 2021-10-17 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_management', '0014_auto_20211014_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselog',
            name='student',
            field=models.ForeignKey(blank=True, help_text='The student corresponding to this course log', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student'),
        ),
    ]
