from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import NewUser


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
        help_text='Введите пароль ещё раз для подтверждения.'
    )
    user_nickname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'},
    ))
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'},
    ))
    user_surname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'},
    ))
    user_sex = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'},
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    about = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = NewUser
        fields = (
            'email',
            'user_nickname',
            'user_name',
            'user_surname',
            'user_sex',
            'user_avatar',
            'about'
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return
