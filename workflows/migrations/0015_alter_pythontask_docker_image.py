# Generated by Django 3.2.5 on 2021-08-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0014_merge_20210821_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythontask',
            name='docker_image',
            field=models.CharField(default='python:3.8-alpine', max_length=255),
        ),
    ]
