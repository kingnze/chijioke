# Generated by Django 4.0.5 on 2022-07-21 14:34

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='stportnews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=False, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2022, 7, 21, 15, 34, 24, 160329))),
                ('leadimg', models.ImageField(default='myleadimg.jpg', upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'stportnews',
                'verbose_name_plural': 'stportnews',
                'db_table': 'stportnews',
                'managed': True,
            },
        ),
    ]
