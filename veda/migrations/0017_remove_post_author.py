# Generated by Django 3.1.1 on 2022-11-08 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veda', '0016_auto_20221108_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]