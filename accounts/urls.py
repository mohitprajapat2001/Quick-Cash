from django.contrib import admin
from django.urls import path, include
from accounts.views import ProfileView, LogoutView, LoginView, RegisterView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("profile/<int:pk>", ProfileView.as_view(), name="profile"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
]
