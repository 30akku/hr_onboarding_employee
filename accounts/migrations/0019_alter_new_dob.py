# Generated by Django 3.2 on 2021-10-01 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_new_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='dob',
            field=models.DateTimeField(null=True),
        ),
    ]
