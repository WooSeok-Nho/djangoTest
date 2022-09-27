# Generated by Django 4.1.1 on 2022-09-27 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesslog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='접속 시간'),
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='location',
            field=models.CharField(max_length=50, verbose_name='접속 경로'),
        ),
    ]
