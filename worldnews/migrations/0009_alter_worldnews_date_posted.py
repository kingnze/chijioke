# Generated by Django 4.0.5 on 2022-12-12 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldnews', '0008_alter_worldnews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 345018)),
        ),
    ]