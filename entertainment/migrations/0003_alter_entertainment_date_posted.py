# Generated by Django 4.0.5 on 2022-08-28 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_alter_entertainment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 15, 8, 54, 76831)),
        ),
    ]
