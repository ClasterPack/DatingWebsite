from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import user_registration, user_login, user_logout, users_list, home_page

app_name = 'users'

urlpatterns = [
    path('', home_page, name='home'),
    path('clients/login', user_login, name='user_login'),
    path('clients/', users_list, name='users_list'),
    path('clients/create/', user_registration, name='user_registration'),
    path('logout/', user_logout, name='user_logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
