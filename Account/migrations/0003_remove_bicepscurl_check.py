# Generated by Django 3.2.9 on 2021-12-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_remove_bicepscurl_total_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicepscurl',
            name='check',
        ),
    ]
