from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_nickname, user_avatar, user_name, user_surname, user_sex, password, **other_fields):
        if not email:
            raise ValueError(_('Вы должны ввести вашу электронную почту.'))
        email = self.normalize_email(email)
        user = self.model(
            email=email, user_nickname=user_nickname,
            user_avatar=user_avatar,
            user_name=user_name, user_surname=user_surname,
            user_sex=user_sex, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_nickname, user_name, user_surname, user_sex, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        return self.create_user(email, user_nickname, user_name, user_surname, user_sex, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):

    SEX_CHOICES = (
        ('m', u"мужской"),
        ('w', u"женский"),
        ('n', u"не выбран"),
    )
    email = models.EmailField(_('электронная почта'), unique=True)
    user_name = models.CharField(_('имя пользователя'), max_length=50)
    user_surname = models.CharField(_('фамилия пользователя'), max_length=50)
    user_nickname = models.CharField(_('ник пользователя'), max_length=50, unique=True)
    user_sex = models.CharField(_('пол'), max_length=1, choices=SEX_CHOICES, default='n')
    user_avatar = models.ImageField(_('аватар пользователя'), default='default.png')
    is_staff = models.BooleanField(_('администратор сайта'), default=False)
    is_active = models.BooleanField(_('активный пользователь'), default=False)
    start_date = models.DateTimeField(_('дата создания пользователя'), default=timezone.now)
    about = models.TextField(_('о себе.'), max_length=500, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_nickname', 'user_name', 'user_surname', 'user_sex']

    def __str__(self):
        return self.user_nickname
