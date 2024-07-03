from django import forms
from .models import Member, Review, Reservation



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title','content', 'image', 'video', 'sustainability_rating']

class SearchForm(forms.Form):
    query = forms.CharField(label='검색', max_length=100)

    
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date','time']