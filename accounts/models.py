from typing import Reversible
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.utils.constants import (
    GENDER_CHOICES,
    CREDIT,
    DEBIT,
    TRANSFER,
    RECEIVE,
)
from django_extensions.db.models import ModificationDateTimeField
from django.db.models import Avg, Q, Sum
from django.utils.timezone import now, timedelta


class Customer(AbstractUser):
    profile = models.ImageField(upload_to="customer_profile", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=132, null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True)
    modified = ModificationDateTimeField()

    def __str__(self):
        return self.username

    def get_account_balance(self):
        return self.account.balance

    def get_todays_money_in_report(self):
        return self.transaction.filter(
            (Q(created__date=now().date()) & Q(transaction_type=CREDIT))
            | (Q(created__date=now().date()) & Q(transaction_type=RECEIVE))
        ).aggregate(sum_amount=Sum("amount"))

    def get_todays_money_out_report(self):
        return self.transaction.filter(
            (Q(created__date=now().date()) & Q(transaction_type=DEBIT))
            | (Q(created__date=now().date()) & Q(transaction_type=TRANSFER))
        ).aggregate(sum_amount=Sum("amount"))

    def get_average_cash_in_report_last_week(self):
        return self.transaction.filter(
            (
                Q(created__date__gte=now().date() - timedelta(days=7))
                & Q(transaction_type=CREDIT)
            )
            | (
                Q(created__date__gte=now().date() - timedelta(days=7))
                & Q(transaction_type=RECEIVE)
            )
        ).aggregate(avg_amount=Avg("amount"))

    def get_average_cash_out_report_last_week(self):
        return self.transaction.filter(
            (
                Q(created__date__gte=now().date() - timedelta(days=7))
                & Q(transaction_type=DEBIT)
            )
            | (
                Q(created__date__gte=now().date() - timedelta(days=7))
                & Q(transaction_type=TRANSFER)
            )
        ).aggregate(avg_amount=Avg("amount"))

    def get_average_receive_report(self):
        return self.transaction.filter(
            Q(transaction_type=CREDIT) | Q(transaction_type=RECEIVE)
        ).aggregate(avg_amount=Avg("amount"))

    def get_average_transfer_report(self):
        return self.transaction.filter(
            Q(transaction_type=DEBIT) | Q(transaction_type=TRANSFER)
        ).aggregate(avg_amount=Avg("amount"))

    def compare_last_week_cash_in_trends(self):
        todays_cash_in = self.get_todays_money_in_report().get("sum_amount")
        weekly_avg_cash_in = self.get_average_cash_in_report_last_week().get(
            "avg_amount"
        )
        if weekly_avg_cash_in != 0:
            difference = todays_cash_in or 0 - weekly_avg_cash_in
            percentage_change = round((difference / weekly_avg_cash_in) * 100, 2)
        return percentage_change or 0

    def compare_last_week_cash_out_trends(self):
        todays_cash_out = self.get_todays_money_out_report().get("sum_amount")
        weekly_avg_cash_out = self.get_average_cash_out_report_last_week().get(
            "avg_amount"
        )
        if weekly_avg_cash_out != 0:
            difference = todays_cash_out or 0 - weekly_avg_cash_out
            percentage_change = round((difference / weekly_avg_cash_out) * 100, 2)
        return percentage_change or 0

    def specific_day_cash_out_amount(self, date):
        amount = (
            self.transaction.filter(
                (Q(created__date=date) & Q(transaction_type=DEBIT))
                | (Q(created__date=date) & Q(transaction_type=TRANSFER))
            )
            .aggregate(sum_amount=Sum("amount"))
            .get("sum_amount")
        )
        return amount or 0

    def specific_day_cash_in_amount(self, date):
        amount = (
            self.transaction.filter(
                (Q(created__date=date) & Q(transaction_type=RECEIVE))
                | (Q(created__date=date) & Q(transaction_type=CREDIT))
            )
            .aggregate(sum_amount=Sum("amount"))
            .get("sum_amount")
        )
        return amount or 0

    def last_7_days_cash_out_report(self):
        queryset = []
        for i in range(0, 7):
            queryset.append(
                self.specific_day_cash_out_amount(now() - timedelta(days=i))
            )
        return queryset

    def last_7_days_cash_in_report(self):
        queryset = []
        for i in range(0, 7):
            queryset.append(self.specific_day_cash_in_amount(now() - timedelta(days=i)))
        return queryset

    class Meta:
        verbose_name = "Banking Customer"
