# Generated by Django 4.0.5 on 2022-12-18 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africanews', '0008_alter_africanews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='africanews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 18, 13, 13, 11, 498244)),
        ),
    ]
