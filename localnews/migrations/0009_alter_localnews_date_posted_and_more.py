# Generated by Django 4.0.5 on 2022-12-14 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localnews', '0008_alter_localnews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localnews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 12, 25, 30, 53836)),
        ),
        migrations.AlterField(
            model_name='localnews',
            name='published',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
