# accountapp/models.py

from django.db import models

class Member(models.Model):
    email = models.CharField(max_length=64, verbose_name='이메일', unique=True)
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    class Meta:
        db_table = 'member'
