# Generated by Django 4.0.5 on 2022-12-19 13:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kingnze', '0007_alter_bigstory_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigstory',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 492134)),
        ),
        migrations.AlterField(
            model_name='business',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 487136)),
        ),
        migrations.AlterField(
            model_name='crime',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 492134)),
        ),
        migrations.AlterField(
            model_name='environment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 492134)),
        ),
        migrations.AlterField(
            model_name='headline',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 487136)),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 497125)),
        ),
        migrations.AlterField(
            model_name='tech',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 497125)),
        ),
        migrations.AlterField(
            model_name='trending',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 49, 22, 497125)),
        ),
        migrations.CreateModel(
            name='TrendingComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Trendingusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.trending')),
            ],
            options={
                'verbose_name': 'TrendingComment',
                'verbose_name_plural': 'TrendingComments',
                'db_table': 'TrendingComments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TechComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Techusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.tech')),
            ],
            options={
                'verbose_name': 'TechComment',
                'verbose_name_plural': 'TechComments',
                'db_table': 'TechComments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HealthComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Healthusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.health')),
            ],
            options={
                'verbose_name': 'HealthComment',
                'verbose_name_plural': 'HealthComments',
                'db_table': 'HealthComments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EnvironmentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Environmentusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.environment')),
            ],
            options={
                'verbose_name': 'EnvironmentComment',
                'verbose_name_plural': 'EnvironmentComments',
                'db_table': 'EnvironmentComments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CrimeCommemt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Crimeusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.crime')),
            ],
            options={
                'verbose_name': 'CrimeComment',
                'verbose_name_plural': 'CrimeComments',
                'db_table': 'CrimeComments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BusinessComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('Businessusercomment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kingnze.business')),
            ],
            options={
                'verbose_name': 'BusinessComment',
                'verbose_name_plural': 'BusinessComments',
                'db_table': 'BusinessComments',
                'managed': True,
            },
        ),
    ]
