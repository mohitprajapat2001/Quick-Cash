import random
from banking.utils.constants import (
    ACCOUNT_NUMBER_END_RANGE,
    ACCOUNT_NUMBER_START_RANGE,
    DEBIT,
    CREDIT,
    TRANSFER,
    RECEIVE,
    DEBIT_TRANSACTION_REMARK,
    CREDIT_TRANSACTION_REMARK,
    TRANSFER_TRANSACTION_REMARK,
    RECEIVE_TRANSACTION_REMARK,
)
from banking.models import Account, Transaction


def generate_account_number() -> int:
    """Generate Random Unique Account Number

    Returns:
        int: account number
    """
    while True:
        account_number = random.randint(
            ACCOUNT_NUMBER_START_RANGE, ACCOUNT_NUMBER_END_RANGE
        )
        if not Account.objects.filter(account_number=account_number):
            return account_number


def create_transaction(customer, amount, transaction_type, remark):
    """create transaction0

    Args:
        customer (_type_): _description_
        amount (_type_): _description_
        transaction_type (_type_): _description_
        remark (_type_): _description_
    """
    Transaction.objects.create(
        customer=customer,
        amount=amount,
        transaction_type=transaction_type,
        remark=remark,
    )


def update_account_balance_post_transaction(
    transaction_type, account_details, amount: int, instance
):
    """update account balance post_save transaction signals

    Args:
        transaction_type :
        account_details :
        instance :
    """
    if transaction_type == DEBIT:
        update_details_for_debit_transaction(account_details, amount, instance)
    elif transaction_type == CREDIT:
        update_details_for_credit_transaction(account_details, amount, instance)


def update_details_for_debit_transaction(account_details, amount, instance):
    """update account details for debit transaction

    Args:
        account_details :
        balance :
    """
    account_details.balance = account_details.balance - amount
    instance.remark = DEBIT_TRANSACTION_REMARK.format(amount=amount)
    account_details.save(update_fields=["balance"])
    instance.save(update_fields=["remark"])


def update_details_for_credit_transaction(account_details, amount, instance):
    """update account details for credit transaction

    Args:
        account_details :
        amount :
    """
    account_details.balance = account_details.balance + amount
    instance.remark = CREDIT_TRANSACTION_REMARK.format(amount=amount)
    account_details.save(update_fields=["balance"])
    instance.save(update_fields=["remark"])


def create_new_transaction_credit_debit(customer, amount: float, transaction_type: str):
    """create new trasaction when user submits the transaction form

    Args:
        customer :
        amount (float): _description_
        transaction_type (str): _description_
    """
    if transaction_type == DEBIT:
        remark = (DEBIT_TRANSACTION_REMARK,)
    elif transaction_type == CREDIT:
        remark = (CREDIT_TRANSACTION_REMARK,)
    create_transaction(
        customer=customer,
        amount=amount,
        transaction_type=transaction_type,
        remark=remark,
    )


def create_new_transaction_transfer_receive_money(
    customer, amount: float, account_number: int
):
    """create new traction for transfer money to receipt account number

    Args:
        customer (_type_): _description_
        amount (float): _description_
        account_number (int): _description_
    """
    sender = Account.objects.get(customer=customer)
    receiver = Account.objects.select_related("customer").get(
        account_number=account_number
    )
    update_details_for_transfer_transaction(sender=sender, amount=amount)
    update_details_for_receive_transaction(receiver=receiver, amount=amount)
    # Create Tranfer Transaction for Sender
    create_transaction(
        customer=customer,
        amount=amount,
        transaction_type=TRANSFER,
        remark=TRANSFER_TRANSACTION_REMARK.format(
            amount=amount, account_number=receiver.account_number
        ),
    )
    # Create Receive Transaction for Receiver
    create_transaction(
        customer=receiver.customer,
        amount=amount,
        transaction_type=RECEIVE,
        remark=RECEIVE_TRANSACTION_REMARK.format(
            amount=amount, account_number=sender.account_number
        ),
    )


def update_details_for_transfer_transaction(sender, amount):
    """update account details for transfer transaction
    Args:
        sender (_type_): _description_
        amount (_type_): _description_
    """
    sender.balance = sender.balance - amount
    sender.save(update_fields=["balance"])


def update_details_for_receive_transaction(receiver, amount):
    """update account details for transfer transaction
    Args:
        receiver (_type_): _description_
        amount (_type_): _description_
    """
    receiver.balance = receiver.balance + amount
    receiver.save(update_fields=["balance"])
