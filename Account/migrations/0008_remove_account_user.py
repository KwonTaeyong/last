# Generated by Django 3.2.9 on 2021-12-20 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20211220_0356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
    ]
