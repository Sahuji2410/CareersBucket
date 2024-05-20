# Generated by Django 5.0.4 on 2024-05-20 20:19

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CareersBucketBaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Updated Date')),
                ('user_type', models.CharField(choices=[], db_index=True, default='User', max_length=10, verbose_name='User Type')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='full name')),
                ('profile_picture', models.ImageField(blank=True, upload_to='', verbose_name='profile picture')),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to=settings.AUTH_USER_MODEL)),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_descriptions', to='apps_models.jobtype')),
            ],
        ),
    ]
