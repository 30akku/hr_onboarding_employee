# Generated by Django 3.2 on 2021-09-29 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210929_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='mname',
        ),
        migrations.RemoveField(
            model_name='new',
            name='nationality',
        ),
    ]
