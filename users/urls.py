from django.urls import path

from users.views import user_registration, user_login, user_logout, users_list

app_name = 'users'

urlpatterns = [
    path('', user_login, name='user_login'),
    path('clients/', users_list, name='users_list'),
    path('clients/create/', user_registration, name='user_registration'),
    path('logout/', user_logout, name='user_logout'),
]
