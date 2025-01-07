# Generated by Django 5.1.4 on 2025-01-07 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_related_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='related_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.chat'),
        ),
    ]
