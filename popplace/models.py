from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

Member = get_user_model()
class Column(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        start_date = models.DateTimeField()
        end_date = models.DateTimeField()
        column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='events')

class PopupStore(models.Model):
    name = models.CharField(max_length=100)
    operating_period = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='popup_images/')
    description = models.TextField()
    latitude = models.FloatField()  # 위도 필드
    longitude = models.FloatField()  # 경도 필드

    def __str__(self):
        return self.name


class Review(models.Model):
    popup_store = models.ForeignKey(PopupStore, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    video = models.FileField(upload_to='review_videos/', null=True, blank=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    sustainability_rating = models.IntegerField()

    def __str__(self):
        return self.title

# class Stamp(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stamps')
    # code = models.CharField(max_length=20)
    # date_received = models.DateTimeField(auto_now_add=True)

# class Favorite(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # popup_store = models.ForeignKey(PopupStore, on_delete=models.CASCADE)

class Popup:
    pass

class Reservation(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    # popup = models.ForeignKey(Popup, on_delete=models.CASCADE)
    popup_store = models.ForeignKey(PopupStore, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()

    # member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='회원')

class ReservationHistory(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)  # ForeignKey로 Member 모델과 연결
    popup_store = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = 'reservation_history'
