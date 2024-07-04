# accountapp/models.py

from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    email = models.CharField(max_length=64, verbose_name='이메일', unique=True)
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    name = models.CharField(max_length=20,verbose_name='이름', null=True, blank=True)
    age = models.CharField(max_length=20,null=True, blank=True, verbose_name='나이')
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_male = models.BooleanField(verbose_name='남성', default=False)
    is_female = models.BooleanField(verbose_name='여성', default=False)

    REQUIRED_FIELDS = []  # 필요한 필드를 여기에 추가
    USERNAME_FIELD = 'email'  # 이메일을 사용하여 사용자를 식별

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    class Meta:
        db_table = 'member'


