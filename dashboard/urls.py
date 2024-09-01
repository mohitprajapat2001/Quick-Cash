from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
]
