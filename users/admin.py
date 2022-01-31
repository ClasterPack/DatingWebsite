from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

from .models import NewUser


class UserAdminConfig(UserAdmin):

    model = NewUser
    search_fields = (
        'email', 'user_name', 'user_surname', 'user_sex',
    )
    list_filter = (
        'email', 'user_name', 'user_surname', 'user_sex',
    )
    ordering = ('-start_date',)
    list_display = (
        'email', 'user_name', 'user_surname', 'user_sex',
        'is_active', 'is_staff', 'start_date',
    )
    fieldsets = (
        ('Персональные Данные', {'fields': (
            'user_name', 'user_surname',
            'user_sex', 'user_avatar', 'about',
        )}),
        ('Разрешения', {'fields': (
            'is_staff', 'is_active',
        )}),
        ('Почта', {'fields': (
            'email',
        )})

    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'user_name', 'user_surname',
                'user_sex', 'user_avatar', 'about',
                'password1', 'password2',
                'is_active', 'is_staff',
            )
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
