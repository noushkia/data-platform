# Generated by Django 3.2.6 on 2021-08-13 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0004_auto_20210811_1251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DockerExecuteTask',
            new_name='DockerTaskExecution',
        ),
    ]
