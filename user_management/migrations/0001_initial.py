# Generated by Django 3.2.3 on 2021-09-14 11:47

import common.model_mixins
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('public_id', models.CharField(blank=True, help_text='Public ID to identify an individual user.', max_length=30, unique=True, verbose_name='Public User ID')),
                ('_role', models.SmallIntegerField(choices=[(4, 'ADMINISTRATOR'), (3, 'STAFF'), (2, 'INSTRUCTOR'), (1, 'STUDENT')], default=1, help_text='The role of the user.', verbose_name='Role')),
                ('send_email', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, help_text='Set to YES if this individual needs to be sent an email.', verbose_name='Send Email')),
                ('need_password', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, help_text='Set to YES if this individual needs to reset their password.', verbose_name='Need Password')),
                ('dob', models.DateField(blank=True, help_text='The date of your birth.', null=True, verbose_name='Date of Birth')),
                ('address', models.TextField(blank=True, help_text='Address', max_length=300, null=True, verbose_name='Address')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not selected', 'Not selected')], default='Not selected', max_length=20, verbose_name='Gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ('last_name', 'username'),
            },
            bases=(common.model_mixins.ValidateOnSaveMixin, models.Model),
            managers=[
                ('members', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
