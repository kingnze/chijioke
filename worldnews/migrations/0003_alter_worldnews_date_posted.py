# Generated by Django 4.0.5 on 2022-08-02 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldnews', '0002_alter_worldnews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 10, 26, 55, 390358)),
        ),
    ]