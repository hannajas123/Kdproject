# Generated by Django 4.0.1 on 2024-02-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='kuris',
            name='installmentamount',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
