# Generated by Django 5.1.2 on 2024-11-05 03:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_task_completed_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
