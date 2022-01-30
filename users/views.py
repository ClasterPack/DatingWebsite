from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.core.handlers.wsgi import WSGIRequest

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
        return redirect('users_list')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users_list')
    return render(request, template_name='base.html', context={'form': form})


def user_registration(request):
    user_register_form = CustomUserCreationForm()
    if request.method == 'POST':
        if user_register_form.is_valid():
            customer: NewUser = user_register_form.save(commit=False)
            customer.save()
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
