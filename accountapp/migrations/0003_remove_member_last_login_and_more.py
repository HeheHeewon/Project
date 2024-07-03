# Generated by Django 4.2.13 on 2024-07-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='member',
            name='registered_dttm',
        ),
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='이름'),
        ),
    ]
