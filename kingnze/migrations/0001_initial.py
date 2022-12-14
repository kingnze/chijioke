# Generated by Django 4.0.5 on 2022-07-11 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
                'managed': True,
            },
        ),
    ]
