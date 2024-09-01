from django.forms import (
    CharField,
    FloatField,
    Form,
    HiddenInput,
    IntegerField,
    NumberInput,
    Select,
    TextInput,
)
from banking.bank_choices import TRANSACTION_FORM_CHOICES


class TransactionForm(Form):
    form_type = CharField(
        widget=HiddenInput(attrs={"class": "form-control", "value": "transaction_form"})
    )
    amount = FloatField(
        required=True,
        widget=NumberInput(attrs={"class": "form-control", "steps": "0.01"}),
        help_text="Amount is Required Field",
        label="Please Enter Amount",
    )
    transaction_type = CharField(
        required=True,
        widget=Select(
            choices=TRANSACTION_FORM_CHOICES, attrs={"class": "form-control"}
        ),
        help_text="Transaction Type is Required Field",
    )


class TransferForm(Form):
    form_type = CharField(
        widget=HiddenInput(attrs={"class": "form-control", "value": "transfer_form"})
    )
    account_number = IntegerField(
        required=True,
        widget=NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
        help_text="Account Number is Required Field",
        label="Please Enter Receiver Account Number",
    )
    amount = FloatField(
        required=True,
        widget=NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        help_text="Amount is Required Field",
        label="Please Enter Amount",
    )
