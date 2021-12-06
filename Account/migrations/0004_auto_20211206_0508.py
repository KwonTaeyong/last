# Generated by Django 3.2.9 on 2021-12-06 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_remove_bicepscurl_check'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TotalNumber',
        ),
        migrations.AlterModelOptions(
            name='bicepscurl',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='squat',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='pushup',
            name='total_time',
        ),
        migrations.RemoveField(
            model_name='squat',
            name='total_time',
        ),
        migrations.AddField(
            model_name='bicepscurl',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pushup',
            name='day',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pushup',
            name='times',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pushup',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='day',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='times',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bicepscurl',
            name='day',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bicepscurl',
            name='times',
            field=models.FloatField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bicepscurl',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pushup',
            name='count',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pushup',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='squat',
            name='count',
            field=models.FloatField(max_length=255),
        ),
    ]