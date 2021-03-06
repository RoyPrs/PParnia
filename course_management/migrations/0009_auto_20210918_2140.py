# Generated by Django 3.2.3 on 2021-09-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0008_auto_20210918_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='courselog',
            name='status',
            field=models.CharField(choices=[('Unavailable', 'Unavailable'), ('Not Approved', 'Not Approved'), ('Approved', 'Approved')], default='Unavailable', help_text='Designates if the grade is not entered, entered or finalized.', max_length=20, verbose_name='Course Status'),
        ),
        migrations.AlterField(
            model_name='courselog',
            name='final_grade',
            field=models.PositiveSmallIntegerField(blank=True, help_text='The final grade of the course', verbose_name='Final Grade'),
        ),
    ]
