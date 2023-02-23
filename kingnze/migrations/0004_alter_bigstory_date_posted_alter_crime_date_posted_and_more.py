# Generated by Django 4.0.5 on 2022-12-12 22:33

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kingnze', '0003_alter_bigstory_date_posted_alter_crime_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigstory',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 337771)),
        ),
        migrations.AlterField(
            model_name='crime',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 337771)),
        ),
        migrations.AlterField(
            model_name='environment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 337771)),
        ),
        migrations.AlterField(
            model_name='headline',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 332777)),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 337771)),
        ),
        migrations.AlterField(
            model_name='trending',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 337771)),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550)),
                ('slug', models.SlugField(blank=True, max_length=550, null=True)),
                ('published', models.BooleanField(blank=True, default=False, null=True)),
                ('flag', models.BooleanField(blank=True, default=False, null=True)),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2022, 12, 12, 23, 33, 38, 332777))),
                ('leadimg', models.ImageField(upload_to='')),
                ('body', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Business',
                'verbose_name_plural': 'Business',
                'db_table': 'Business',
                'managed': True,
            },
        ),
    ]