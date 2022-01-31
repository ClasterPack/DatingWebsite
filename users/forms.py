from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import NewUser
from .sex_choices import Sex


class CustomUserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': 'Пароли не совпадают.'
    }
    password1 = forms.CharField(
        label='Пароль.',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label='Подтверждение пароля.',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    user_name = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        help_text='Введите имя.'
    )
    user_surname = forms.CharField(
        required=True, widget=forms.TextInput(
            attrs={'class': 'form-control'}),
        help_text='Введите фамилию.'

    )
    user_sex = forms.ChoiceField(
        required=True,
        choices=Sex.choices,
        help_text='Выберите пол'
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    about = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    # user_avatar = forms.ImageField()

    class Meta:
        model = NewUser
        fields = (
            'email',
            'user_name',
            'user_surname',
            'user_sex',
            'user_avatar',
            'about',
        )
        widgets = {
            'sex': forms.Select(attrs={'class': 'custom-select md-form'}),
        }

