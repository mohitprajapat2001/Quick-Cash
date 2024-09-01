from django.contrib import admin
from banking.models import Transaction, Account


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["transaction_id", "customer", "transaction_type"]
    readonly_fields = ["id", "transaction_id", "created", "modified"]
    fieldsets = [
        (
            "Transaction Details",
            {
                "fields": [
                    "id",
                    "transaction_id",
                    "transaction_type",
                    "amount",
                    "customer",
                    "remark",
                ]
            },
        ),
        (
            "Timestamp Details",
            {"classes": ["collapse"], "fields": ["created", "modified"]},
        ),
    ]
    search_fields = ["transaction_id", "customer__username"]
    list_filter = ["created", "transaction_type"]
    ordering = ["-created"]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "account_number", "balance"]
    readonly_fields = ["id", "created", "modified"]
    fieldsets = [
        (
            "Account Details",
            {"fields": ["id", "customer", "account_number", "balance"]},
        ),
        (
            "Timestamp Details",
            {"classes": ["collapse"], "fields": ["created", "modified"]},
        ),
    ]
    search_fields = ["id", "customer__username", "account_number"]
    list_filter = ["created", "modified"]
    ordering = ["id", "customer"]
