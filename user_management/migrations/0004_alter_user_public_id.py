# Generated by Django 3.2.3 on 2021-10-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_id',
            field=models.CharField(blank=True, editable=False, help_text='Public ID to identify an individual user.', max_length=30, unique=True, verbose_name='Public User ID'),
        ),
    ]
