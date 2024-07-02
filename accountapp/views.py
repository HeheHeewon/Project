from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accountapp.forms import MemberForm, LoginForm
from accountapp.models import Member

res_data = {}

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = MemberForm(request.POST)
        email=request.POST['email']
        password = request.POST['password']
        lenpwd=len(password)
        checkpwd = request.POST['checkpwd']
        if not (email and password and checkpwd):
            res_data['error_msg'] = "모든 값을 입력해야 합니다."
        elif (password != checkpwd):
            res_data['error_msg'] = '비밀번호가 다릅니다.'
        elif Member.objects.filter(email=email).exists():
            res_data['error_msg']='동일한 이메일로 가입한 회원이 있습니다.'
        elif (lenpwd<8 or lenpwd>20):
            res_data['error_msg']='비밀번호는 8자리 이상, 20자리 이하로 설정하세요.'
        elif form.is_valid():
            email1 = form.clean_email()
            form = Member(email=email1, password=make_password(password))
            form.save()
            return redirect('/account/login')
    return render(request, 'accountapp/signup.html', res_data)



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