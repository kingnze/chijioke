# Generated by Django 4.0.5 on 2022-09-03 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('africanews', '0003_alter_africanews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='africanews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 3, 10, 10, 23, 78287)),
        ),
    ]
