from django.apps import AppConfig


class BankingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "banking"

    def ready(self):
        from banking.signals import (
            create_account_details_for_new_user,
            update_accounts_details_based_on_transactions,
        )
