# Generated by Django 4.0.5 on 2022-12-19 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localnews', '0010_alter_localnews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 1, 54, 53, 735426)),
        ),
    ]
