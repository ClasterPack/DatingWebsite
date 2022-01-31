from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q

from typing import Dict, Optional

from users.forms import CustomUserCreationForm
from users.models import NewUser
from django.contrib.auth.forms import AuthenticationForm


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)
    return HttpResponse(status=405)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('users/home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users:home')
    return render(request, template_name='user/user_login.html', context={'form': form})


def user_registration(request):
    user_register_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_register_form: CustomUserCreationForm = CustomUserCreationForm(request.POST, files=request.FILES)
        if user_register_form.is_valid():
            user: NewUser = user_register_form.save(commit=False)
            sex = request.POST.get('user_sex')
            user.user_sex = sex
            avatar = request.POST.get('user_avatar')
            user.user_avatar = avatar
            user.save()
            user_register_form.save()
            return redirect('users:user_login')

    return render(
        request,
        template_name='user/registration.html',
        context={
            'form': user_register_form,
        }
    )


def users_list(request: WSGIRequest) -> HttpResponse:
    pass
    # user_q = Q()
    # order_q = Q()
    # q = request.get('q')
    #
    # if q:
    #     user_q &= Q(user_name__incontains=q) | Q(user_surname__icontains=q)
    #     order_q &= Q(user_name__incontains=q[-1]) | Q(user_surname__icontains=q[-1])
    #
    # order_info: Dict[]
    #


def home_page(request):
    return render(request, template_name='base.html')

