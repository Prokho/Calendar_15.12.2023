# Generated by Django 4.2.2 on 2023-12-24 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0016_alter_appointment_time_appointment_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 21, 25, 38, 644840)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='token',
            field=models.CharField(default='nKPCQ3mRm3jNhkAmJgsryOUTgKBMkn2c06V6Z_iYedY', max_length=200),
        ),
    ]
