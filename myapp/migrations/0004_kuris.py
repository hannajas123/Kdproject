# Generated by Django 4.0.1 on 2023-12-05 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_k_dmembers_email_kmembers_meetig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kuris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('totalAmount', models.CharField(max_length=100)),
                ('totalinstallments', models.CharField(max_length=100)),
                ('startingDate', models.DateField()),
                ('EndingDate', models.DateField()),
                ('KDUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit')),
            ],
        ),
    ]