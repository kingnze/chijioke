# Generated by Django 4.0.5 on 2022-08-27 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africanews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='africanews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 27, 14, 56, 26, 11869)),
        ),
    ]
