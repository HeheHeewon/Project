# Generated by Django 4.2.13 on 2024-07-04 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_stamp_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='stamp',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stamps/'),
        ),
    ]
