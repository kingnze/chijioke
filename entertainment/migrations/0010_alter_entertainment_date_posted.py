# Generated by Django 4.0.5 on 2022-12-19 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0009_alter_entertainment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 1, 54, 53, 742345)),
        ),
    ]
