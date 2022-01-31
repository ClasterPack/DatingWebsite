from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .sex_choices import Sex
from .watermark import add_watermark


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, user_name, user_surname, user_sex, user_avatar, password, **extra_fields):
        if not email:
            raise ValueError(_('Нужна электронная почта.'))

        email = self.normalize_email(email)
        user_avatar = add_watermark(user_avatar)
        user = self.model(
            email=email, user_name=user_name,
            user_surname=user_surname, user_sex=user_sex,
            user_avatar=user_avatar, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, user_surname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_avatar', 'avatars/default.png')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )
        return self.create_user(email,  user_name, user_surname, password, **extra_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('электронная почта'), unique=True)
    user_name = models.CharField(_('имя пользователя'), max_length=50)
    user_surname = models.CharField(_('фамилия пользователя'), max_length=50)
    user_sex = models.PositiveSmallIntegerField(choices=Sex.choices, default='-')
    user_avatar = models.ImageField(_('аватар пользователя'), upload_to='')
    is_staff = models.BooleanField(_('администратор сайта'), default=False)
    is_active = models.BooleanField(_('активный пользователь'), default=False)
    start_date = models.DateTimeField(_('дата создания пользователя'), default=timezone.now)
    about = models.TextField(_('о себе.'), max_length=500, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'user_surname']

    def __str__(self):
        full_name = f'{self.user_name} {self.user_surname}'
        return full_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'