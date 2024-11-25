from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms


class RegisterUserForm(UserCreationForm):
    """
    Форма реєстрації новго користувача
    """
    username = forms.CharField(label='Логін', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Підтвердження пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'email': "E-mail",
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        """
        Перевірка на унікальність електронної пошти
        :return: email
        """
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такий E-mail вже існує")
        return email


class LoginUserForm(AuthenticationForm):
    """
    Форма авторизації. Використовується вбудована з класу LoginView
    """
    username = forms.CharField(label='Логін',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()  # Використовуємо поточну модель користувача, тому що стандартна модель User може бути змінена.
        fields = ['username', 'password']


class UserPasswordChangeForm(PasswordChangeForm):
    """
    Форма зміни пароля. Використовується вбудований клас PasswordChangeForm
    """
    old_password = forms.CharField(label="Старий пароль",
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    new_password1 = forms.CharField(label="Новий пароль",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    new_password2 = forms.CharField(label="Підтвердити пароль",
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'})),
