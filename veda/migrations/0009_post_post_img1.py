# Generated by Django 3.1.1 on 2021-03-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veda', '0008_auto_20210226_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]