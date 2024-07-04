# models.py

from django.db import models
from django.contrib.auth import get_user_model
from .models import PopupStore

class PopupStore(models.Model):
    name = models.CharField(max_length=100, verbose_name='팝업스토어 이름')
    location = models.CharField(max_length=200, verbose_name='위치')

    def __str__(self):
        return self.name

class PopupReservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='popup_reservations',
                                 verbose_name='사용자')
    popup_store = models.ForeignKey(PopupStore, on_delete=models.CASCADE, related_name='reservations',
                                        verbose_name='팝업스토어')
    date = models.DateField(verbose_name='날짜')
    time = models.TimeField(verbose_name='시간')

    def __str__(self):
        return f'{self.user} - {self.popup_store} - {self.date} {self.time}'
