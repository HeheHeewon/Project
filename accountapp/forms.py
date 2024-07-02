import django.contrib.auth.forms as auth_forms
from django import forms
from accountapp.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            self.add_error('email', '이미 가입된 이메일입니다.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=64, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password = forms.CharField(
        max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
