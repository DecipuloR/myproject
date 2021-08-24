# Generated by Django 3.1.6 on 2021-08-22 01:09

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
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default=None, max_length=100, null=True)),
                ('lastName', models.CharField(default=None, max_length=100, null=True)),
                ('middleName', models.CharField(default=None, max_length=100, null=True)),
                ('disability', models.CharField(choices=[('Psychosocial Disability', 'psychosocial disability'), ('Chronic Illness', 'chronic illness'), ('Learning Disability', 'learning disability'), ('Mental Disability', 'mental disability'), ('Visual Disability', 'visual disability'), ('Orthopedic Disability', 'orthopedic disability'), ('Communication Disability', 'communication disability')], max_length=200, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField(default=0, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=100, null=True)),
                ('ContactNumber', models.CharField(max_length=100, null=True)),
                ('BirthDate', models.DateField(default=None, null=True)),
                ('DateUpdated', models.DateField(default=None, null=True)),
                ('File', models.ImageField(null=True, upload_to='media')),
                ('COIFile', models.FileField(null=True, upload_to='media')),
                ('MCFile', models.FileField(null=True, upload_to='media')),
                ('status', models.CharField(choices=[('Approved', 'approved'), ('Denied', 'denied')], default='Pending', max_length=100, null=True)),
                ('Pwdnumber', models.CharField(default='Pending', max_length=12)),
            ],
            options={
                'db_table': 'Applicants info.',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostAnnouncement', models.TextField(default='No Announcement yet.', null=True)),
            ],
            options={
                'db_table': 'POST',
            },
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, null=True)),
                ('message', models.TextField(default=None, null=True)),
                ('email', models.ForeignKey(blank=True, db_column='email', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
