# Generated by Django 4.2 on 2023-07-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoapp',
            name='body',
            field=models.TextField(default='1. #Todo goes here'),
        ),
    ]