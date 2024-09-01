from django.contrib import admin
from accounts.models import Customer
from accounts.utils.constants import (
    USER_STATUS_FALSE,
    USER_STATUS_TRUE,
    CUSTOMER_ADMIN_STATUS_UNACTIVE_DESCRIPTION,
    CUSTOMER_ADMIN_STATUS_ACTIVE_DESCRIPTION,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_active", "is_superuser"]
    readonly_fields = ["id"]
    fieldsets = [
        (
            "Customer Details",
            {
                "fields": [
                    "id",
                    "profile",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                    "age",
                    "gender",
                    "address",
                    "phone",
                ]
            },
        ),
        (
            "Status Details",
            {
                "classes": ["collapse"],
                "fields": ["is_staff", "is_superuser", "is_active"],
            },
        ),
        (
            "Login Details",
            {"classes": ["collapse"], "fields": ["date_joined", "last_login"]},
        ),
        (
            "Group Details",
            {"classes": ["collapse"], "fields": ["groups", "user_permissions"]},
        ),
    ]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    ordering = ["id"]
    actions = ["mark_inactive", "mark_active"]

    @admin.action(description=CUSTOMER_ADMIN_STATUS_UNACTIVE_DESCRIPTION)
    def mark_inactive(self, request, queryset):
        for instantce in queryset:
            instantce.is_active = USER_STATUS_FALSE
            instantce.save(update_fields=["is_active"])

    @admin.action(description=CUSTOMER_ADMIN_STATUS_ACTIVE_DESCRIPTION)
    def mark_active(self, request, queryset):
        for instantce in queryset:
            instantce.is_active = USER_STATUS_TRUE
            instantce.save(update_fields=["is_active"])
