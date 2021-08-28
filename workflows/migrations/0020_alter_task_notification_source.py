# Generated by Django 3.2.6 on 2021-08-25 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_alter_notificationsource_user'),
        ('workflows', '0019_alter_task_accessible_datasets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notification_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notifications.notificationsource'),
        ),
    ]