# Generated by Django 3.0.7 on 2020-07-03 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('personnel_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('email_adress', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
    ]
