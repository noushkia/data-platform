# Generated by Django 3.2.6 on 2021-08-09 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0004_merge_20210808_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='is_public',
        ),
    ]
