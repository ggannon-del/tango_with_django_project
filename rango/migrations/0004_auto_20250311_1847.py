# Generated by Django 2.2.28 on 2025-03-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_delete_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
