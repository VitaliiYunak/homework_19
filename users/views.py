from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.db import connection
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import LoginUserForm, RegisterUserForm, UserPasswordChangeForm


def logout_user(request):
    """
    Функція викликає метод logout(request) для виходу користувача із системи.
    """
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def index(request):
    """
    Сторінка доступна тільки для авторизованих користувачів
    """
    context = {'title': 'Домашня сторінка'}
    return render(request, 'users/index.html', context)


class LoginUser(LoginView):
    """
    Авторизація. Використовується форма  LoginUserForm
    """
    template_name = 'users/login.html'
    form_class = LoginUserForm
    extra_context = {'title': 'Авторизація'}

    def get_success_url(self):
        """ Перехід на сторінку при успішній авторизації
            Альтернатива: у файлі settings.py вказати LOGIN_REDIRECT_URL='home'. Додатково у html файлі необхідно
            вказати приховане поле {{ next }}
        """
        return reverse_lazy('home')


class RegisterUser(CreateView):
    """
    Рєстрація нового користувача
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {"title": "Реєстрація користувача"}
    success_url = reverse_lazy('login')


class UserPasswordChange(PasswordChangeView):
    """
    Змінити пароль
    """
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('password_change_done')
    extra_context = {"title": "Змінити пароль"}


# Функція для безпечного виконання SQL-запитів
def get_user_by_email(email):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM auth_user WHERE email = %s", [email])
        return cursor.fetchone()