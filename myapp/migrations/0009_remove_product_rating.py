# Generated by Django 4.0.1 on 2023-12-05 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_notification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]