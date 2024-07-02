# Generated by Django 4.2.13 on 2024-07-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='최근 로그인 시간')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='가입 일자')),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
