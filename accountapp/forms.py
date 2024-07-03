import django.contrib.auth.forms as auth_forms
from django import forms
from accountapp.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'password', 'name', 'age', 'is_male', 'is_female']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            self.add_error('email', '이미 가입된 이메일입니다.')
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('이름을 입력해주세요.')
        return name

    def clean(self):
        cleaned_data = super().clean()
        is_male = cleaned_data.get('is_male')
        is_female = cleaned_data.get('is_female')

        # 둘 다 선택된 경우 에러 발생
        if is_male and is_female:
            raise forms.ValidationError('남성 또는 여성 중 하나만 선택해야 합니다.')
        return cleaned_data

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=64, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password = forms.CharField(
        max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
