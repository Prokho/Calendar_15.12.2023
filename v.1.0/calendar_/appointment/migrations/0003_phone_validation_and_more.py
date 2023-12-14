# Generated by Django 4.1 on 2022-10-10 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_time_appointment_create_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone_validation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('validation_code', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 20, 18, 27, 148748)),
        ),
    ]