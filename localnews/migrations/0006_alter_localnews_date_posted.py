# Generated by Django 4.0.5 on 2022-12-09 15:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localnews', '0005_alter_localnews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 16, 33, 59, 851293)),
        ),
    ]
