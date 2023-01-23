# Generated by Django 4.1.3 on 2022-12-12 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'sys_notification_logs',
            },
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('body', models.TextField()),
                ('recepients', models.JSONField()),
                ('cc', models.JSONField(null=True)),
                ('bcc', models.JSONField(null=True)),
                ('is_sent', models.BooleanField(default=False)),
                ('sent_at', models.DateTimeField(null=True)),
                ('failure_reason', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('notification', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationlog')),
            ],
            options={
                'db_table': 'sys_email_logs',
            },
        ),
    ]
