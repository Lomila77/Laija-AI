# Generated by Django 5.0.6 on 2024-06-16 17:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0001_create_ai_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ai',
            unique_together={('user', 'name')},
        ),
    ]
