# Generated by Django 3.2.3 on 2021-10-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_remove_user__role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='Password', max_length=128, verbose_name='password'),
        ),
    ]
