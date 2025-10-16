from django.contrib.auth import logout, login
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("api/register/", views.RegisterApi.as_view()),
    path("register/", views.RegisterView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("getme/", views.GetMeApi.as_view()),
    
]