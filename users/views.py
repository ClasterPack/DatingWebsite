from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from users.forms import CustomUserCreationForm
from users.models import NewUser


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)
    return HttpResponse(status=405)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('users:users_list')
    return render(request, template_name='user/user_login.html', context={'form': form})


def user_registration(request):
    # if request.POST:
    #     form: CustomUserCreationForm = CustomUserCreationForm(request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         email = request.POST.get('email')
    #         password = request.POST.get('password')
    #         account = authenticate(email=email, password=password)
    #         login(request, account)
    #         return redirect('user:users_login')
    #     else:
    #         context = {'form': form}
    # else:
    #     user_register_form = CustomUserCreationForm()
    #     context = {'form': user_register_form}
    # return render(request, 'user/registration.html', context)
    user_register_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_register_form: CustomUserCreationForm = CustomUserCreationForm(request.POST, files=request.FILES)
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
    user_q = Q()
    order_q = Q()
    q = request.GET.get('q')

    if q:
        user_q &= Q(user_name__incontains=q) | Q(user_surname__icontains=q) | Q(user_sex=q)
        order_q &= Q(user_name__incontains=q[-1]) | Q(user_surname__icontains=q[-1]) | Q(user_sex=q)

    context = {
        'users': NewUser.objects.filter(is_active=True).filter(user_q).annotate(user_count=Count('user_name'))
    }
    return render(request, 'user/users_list.html', context=context)


def home_page(request):
    return render(request, template_name='base.html')

