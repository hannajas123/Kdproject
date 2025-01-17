# Generated by Django 4.0.1 on 2023-11-22 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('theme', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='K_dmembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('panchayath', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='K_dunit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit_no', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('panchayath', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Meetig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('purpose', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notification', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('KDUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=200)),
                ('datails', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('quality', models.CharField(max_length=100)),
                ('KDUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=500)),
                ('place', models.CharField(max_length=100)),
                ('panchayath', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Return_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('winner', models.CharField(max_length=200)),
                ('KDMEMBER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dmembers')),
                ('KDUNIT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit')),
            ],
        ),
        migrations.CreateModel(
            name='Order_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('ORDERMAIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order_main')),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='order_main',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='k_dunit',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
        migrations.AddField(
            model_name='k_dmembers',
            name='KDUNIT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.k_dunit'),
        ),
        migrations.AddField(
            model_name='k_dmembers',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feedback', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('complaint', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
