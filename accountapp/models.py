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

    class Meta:
        db_table = 'member'

class Stamp(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)  # 아이콘 정보를 저장할 필드
    stamp_code = models.CharField(max_length=20)  # 도장 정보에 대한 필드 추가 가능
    timestamp = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    popup_info = models.TextField()

class Favorite(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    popup_list = models.TextField()




