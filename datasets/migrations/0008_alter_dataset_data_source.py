# Generated by Django 3.2.6 on 2021-09-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0007_auto_20210904_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datasets.datasource'),
        ),
    ]