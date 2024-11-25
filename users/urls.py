# from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views
from .views import UserPasswordChange

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.LoginUser.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'), # Через клас LogoutView
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name='password_change_done'),
]
