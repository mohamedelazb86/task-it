from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='authuser'

urlpatterns = [
    path('login',login_required(views.LoginView.as_view()),name='login'),
    path('all_user',login_required(views.all_user),name='all_user'),
]
