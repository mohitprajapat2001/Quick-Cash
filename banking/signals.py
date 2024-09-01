from django.db.models.signals import post_save
from django.dispatch import receiver
from banking.models import Transaction, Customer, Account
from accounts.models import Customer
from banking.utils import (
    generate_account_number,
    update_account_balance_post_transaction,
)
from banking.constants import NEW_ACCOUNT_REMARK


@receiver(post_save, sender=Transaction)
def update_accounts_details_based_on_transactions(
    sender, instance, created, *args, **kwargs
):
    if created:
        customer = instance.customer
        account_details = Account.objects.get(customer=customer)
        update_account_balance_post_transaction(
            transaction_type=instance.transaction_type,
            account_details=account_details,
            amount=instance.amount,
            instance=instance,
        )


@receiver(post_save, sender=Customer)
def create_account_details_for_new_user(sender, instance, created, *args, **kwargs):
    if created:
        Account.objects.create(
            customer=instance, account_number=generate_account_number()
        )
        Transaction.objects.create(
            customer=instance,
            remark=NEW_ACCOUNT_REMARK.format(customer=instance),
        )
