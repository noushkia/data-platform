# Generated by Django 3.2.6 on 2021-08-09 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workflows', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image_url',
        ),
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='docker_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('N', 'None'), ('R', 'Running'), ('F', 'Failed'), ('S', 'Stopped')], default='N', max_length=1),
        ),
    ]