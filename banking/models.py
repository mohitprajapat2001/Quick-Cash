from django.db import models
from django_extensions.db.models import TimeStampedModel
from banking.utils.bank_choices import TRANSACTION_TYPE_CHOICES
from banking.utils.constants import (
    BALANCE_DEFAULT,
    BANK_ONE2ONE_CUSTOMER,
    TRANSACTION_FK_CUSTOMER,
    ACCOUNT_ONE2ONE_CUSTOMER,
)
from accounts.models import Customer
import uuid


class Account(TimeStampedModel):
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name=ACCOUNT_ONE2ONE_CUSTOMER
    )
    account_number = models.BigIntegerField()
    balance = models.FloatField(default=BALANCE_DEFAULT)


class Transaction(TimeStampedModel):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name=TRANSACTION_FK_CUSTOMER
    )
    amount = models.FloatField(default=0)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE_CHOICES)
    remark = models.CharField(null=True, blank=True)

    def __str__(self):
        return "{customer}'s transaction of {transaction_type} with {transaction_id}".format(
            customer=self.customer,
            transaction_type=self.transaction_type,
            transaction_id=self.transaction_id,
        )

    class Meta:
        ordering = ["-created"]
