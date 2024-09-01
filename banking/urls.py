import time
from django.contrib import admin
from django.urls import path, include
from banking.views import Transactions, BankingServices
from django.views.decorators.cache import cache_page

urlpatterns = [
    path(
        "", cache_page(timeout=300)(BankingServices.as_view()), name="banking_services"
    ),
    path("transactions", Transactions.as_view(), name="transactions"),
]
