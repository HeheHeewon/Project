from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import CustomAuthenticationForm, CustomUserCreationForm, ReservationForm


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/accounts/signdone')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/accounts/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

def signdone(request):
    return render(request, 'accounts/signdone.html')
def home(request):
    return render(request, 'accounts/home.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Reservation, Stamp, PopupStore


@login_required
def mypage(request):
    user = request.user

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    reservations = Reservation.objects.filter(user=user)
    stamps_count = Stamp.objects.filter(user=user).count()
    stamps = user.stamps.all()

    context = {
        'user': user,
        'profile': profile,
        'reservations': reservations,
        'stamps_count': stamps_count,
        'stamps': stamps,
    }

    return render(request, 'accounts/mypage.html', context)

@login_required
def add_stamp(request):
    if request.method == 'POST':
        authentication_code = request.POST.get('authentication_code')

        # 예시로 설정된 인증 번호들 (실제 사용 시 데이터베이스 조회 등으로 처리해야 함)
        valid_authentication_codes = ['1234', '5678', '9999']

        if authentication_code in valid_authentication_codes:
            # 인증 번호가 일치할 경우 도장 추가
            user = request.user
            stamp = Stamp(user=user)
            stamp.save()

            # stamps_count 1 증가
            stamps_count = Stamp.objects.filter(user=user).count()

            messages.success(request, '도장이 추가되었습니다.')
            return redirect('/accounts/mypage')
        else:
            messages.error(request, '인증 번호가 올바르지 않습니다.')

    return render(request, 'accounts/add_stamp.html')

@login_required
def popupreserv(request, popup_id):
    popup = get_object_or_404(PopupStore, id=popup_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.popup_store = popup
            reservation.user = request.user  # 현재 로그인한 사용자를 예약에 저장
            reservation.save()
            return redirect('/accounts/mypage')
    else:
        form = ReservationForm()

    context = {
        'popup': popup,
        'form': form,
    }
    return render(request, 'accounts/popupreserv.html', context)
