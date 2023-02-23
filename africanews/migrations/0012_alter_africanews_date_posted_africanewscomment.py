# Generated by Django 4.0.5 on 2022-12-19 14:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('africanews', '0011_alter_africanews_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='africanews',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 15, 26, 16, 461046)),
        ),
        migrations.CreateModel(
            name='africanewsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('africanewsusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='africanews.africanews')),
            ],
            options={
                'verbose_name': 'africanewsComment',
                'verbose_name_plural': 'africanewsComments',
                'db_table': 'africanewsComments',
                'managed': True,
            },
        ),
    ]