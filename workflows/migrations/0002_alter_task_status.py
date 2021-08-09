# Generated by Django 3.2.6 on 2021-08-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('none', 'none'), ('running', 'running'), ('failed', 'failed'), ('stopped', 'stopped')], default='none', max_length=10),
        ),
    ]
