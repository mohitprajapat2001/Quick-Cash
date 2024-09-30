from django.contrib.messages import info
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from requests import get
from banking.utils.constants import (
    TRANSACTION_TEMPLATE,
    TRANSACTIONS_CONTEXT_OBJECT_NAME,
    BANKING_TEMPLATE,
    DEBIT_TRANSACTION_REMARK,
)
from banking.models import Transaction
from banking.forms import TransactionForm, TransferForm
from banking.utils.utils import (
    create_new_transaction_credit_debit,
    create_new_transaction_transfer_receive_money,
)
from django.contrib.messages import info


class Transactions(ListView):
    template_name = TRANSACTION_TEMPLATE
    model = Transaction
    context_object_name = TRANSACTIONS_CONTEXT_OBJECT_NAME
    paginate_by = 10

    def get_queryset(self):
        return Transaction.objects.filter(customer__pk=self.request.user.id)


class BankingServices(TemplateView, FormView):
    template_name = BANKING_TEMPLATE

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        transaction_form = TransactionForm()
        transfer_form = TransferForm()
        return self.render_to_response(
            {"transaction_form": transaction_form, "transfer_form": transfer_form}
        )

    def post(self, request):
        try:
            amount = float(request.POST.get("amount"))
            if request.POST.get("form_type") == "transaction_form":
                transaction_type = request.POST.get("transaction_type")
                create_new_transaction_credit_debit(
                    customer=request.user,
                    amount=amount,
                    transaction_type=transaction_type,
                )
                info(
                    request,
                    "Completed {transaction_type} of RS {amount}".format(
                        transaction_type=transaction_type, amount=amount
                    ),
                )
            elif request.POST.get("form_type") == "transfer_form":
                account_number = request.POST.get("account_number")
                create_new_transaction_transfer_receive_money(
                    customer=request.user, amount=amount, account_number=account_number
                )
                info(
                    request,
                    "Tranfered RS {amount} to Account Number {account_number}".format(
                        amount=amount, account_number=account_number
                    ),
                )
            return redirect("/banking")
        except Exception as err:
            info(request, "Exception Occured: {err}".format(err=err))
            return redirect("/banking")
