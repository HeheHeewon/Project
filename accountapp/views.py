from django.contrib import auth, messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accountapp.forms import MemberForm, LoginForm
from accountapp.models import Member


# res_data = {}

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        checkpwd = request.POST.get('checkpwd')

        # 추가적인 비밀번호 검증 로직
        if not (email and password and checkpwd):
            messages.error(request, "모든 값을 입력해야 합니다.")
        elif password != checkpwd:
            messages.error(request, '비밀번호가 다릅니다.')
        elif Member.objects.filter(email=email).exists():
            messages.error(request, '동일한 이메일로 가입한 회원이 있습니다.')
        elif len(password) < 8 or len(password) > 20:
            messages.error(request, '비밀번호는 8자리 이상, 20자리 이하로 설정하세요.')
        else:
            # 비밀번호 해싱
            hashed_password = make_password(password)
            # 폼을 저장하여 Member 객체 생성 및 저장
            member = form.save(commit=False)
            member.password = hashed_password
            member.save()

            # 회원가입 후 자동으로 로그인 처리
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('account/signdone/')  # 리다이렉트 URL 패턴 이름 사용

    else:
        form = UserCreationForm()

    return render(request, 'accountappp/signup.html', {'form': form})

def signdone(request):
    return render(request, 'accountapp/signdone.html')

        # elif form.is_valid():
            # email1 = form.clean_email()
            # form = Member(email=email1, password=make_password(password))
            # form.save()
            # return redirect('/account/login')
   # return render(request, 'accountapp/signup.html', res_data)

def login_view(request):
    is_ok = False
    msg = None  # Initialize msg to None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            msg = "올바른 유저ID와 패스워드를 입력하세요."
            try:
                user = Member.objects.get(email=email)
            except Member.DoesNotExist:
                msg = "사용자가 존재하지 않습니다."
            else:
                if check_password(raw_password, user.password):
                    login(request, user=user)
                    msg = "로그인 성공!!"
                    is_ok = True
                    # 로그인 성공 시
                    return redirect('/account/signdone')
                else:
                    msg = "패스워드가 올바르지 않습니다."
        else:
            msg = "폼이 유효하지 않습니다. 입력된 데이터를 확인하세요."
    else:
        form = LoginForm()

    return render(request, "accountapp/login.html", {"form": form, "msg": msg, "is_ok": is_ok})

def logout_view(request):
    logout(request)
    return redirect('/account/login')

def sign_done(request):
    return render(request, 'accountapp/signdone.html')

@login_required
def my_page(request):
    user = request.user
    return render(request, 'accountapp/my_page.html', {'user': user})
