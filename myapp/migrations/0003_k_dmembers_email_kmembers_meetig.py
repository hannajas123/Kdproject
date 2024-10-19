# Generated by Django 4.0.1 on 2023-12-05 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_meetig_kdunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='k_dmembers',
            name='Email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='kmembers_Meetig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('purpose', models.CharField(max_length=200)),
                ('KDUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit')),
            ],
        ),
    ]