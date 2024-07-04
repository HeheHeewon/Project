# accountapp/models.py
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        이메일과 비밀번호로 사용자를 생성합니다.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        관리자(superuser) 권한을 가진 사용자 생성합니다.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Member(AbstractBaseUser):
    email = models.CharField(max_length=64, verbose_name='이메일', unique=True)
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    name = models.CharField(max_length=20,verbose_name='이름', null=True, blank=True)
    age = models.CharField(max_length=20,null=True, blank=True, verbose_name='나이')

    is_male = models.BooleanField(verbose_name='남성', default=False)
    is_female = models.BooleanField(verbose_name='여성', default=False)

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    REQUIRED_FIELDS = []  # 필요한 필드를 여기에 추가
    USERNAME_FIELD = 'email'  # 이메일을 사용하여 사용자를 식별

    objects = MemberManager()

    class Meta:
        db_table = 'member'

    def __str__(self):
            return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_lable):
        return True

class Profile(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f'프로필 - {self.user.email}'


class Stamp(models.Model):
    number = models.CharField(max_length=50, null=True)  # 도장 번호
    user = models.ManyToManyField(Member, related_name='stamps')
    icon = models.ImageField(upload_to='stamp_icons/', null=True, blank=True)
    # 추가된 필드: 도장 개수
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.number

class Reservation(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    popup_info = models.TextField()

class Favorite(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    popup_list = models.TextField()


