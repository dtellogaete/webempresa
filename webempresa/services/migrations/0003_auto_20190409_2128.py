# Generated by Django 2.2 on 2019-04-10 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190403_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
    ]
