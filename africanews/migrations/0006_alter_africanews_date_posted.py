# Generated by Django 4.0.5 on 2022-12-09 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africanews', '0005_alter_africanews_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='africanews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 17, 10, 25, 835991)),
        ),
    ]
