from django.contrib import admin

from .models import PopupStore
from .models import Reservation

admin.site.register(PopupStore)
admin.site.register(Reservation)
