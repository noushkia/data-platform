# Generated by Django 3.2.6 on 2021-08-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_auto_20210815_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='datasets', to='datasets.Tag'),
        ),
    ]
