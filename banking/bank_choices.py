from banking.constants import (
    DEBIT,
    DEBIT_TEXT,
    CREDIT,
    CREDIT_TEXT,
    TRANSFER,
    TRANSFER_TEXT,
    RECEIVE,
    RECEIVE_TEXT,
    CREATE,
    CREATE_TEXT,
    SELECT_PLACEHOLDER,
    TRANSACTION_CHOICE_PLACEHOLDER_TEXT,
)

# Bank Models Choices
TRANSACTION_TYPE_CHOICES = (
    (DEBIT, DEBIT_TEXT),
    (CREDIT, CREDIT_TEXT),
    (TRANSFER, TRANSFER_TEXT),
    (RECEIVE, RECEIVE_TEXT),
    (CREATE, CREATE_TEXT),
)

TRANSACTION_FORM_CHOICES = (
    (SELECT_PLACEHOLDER, TRANSACTION_CHOICE_PLACEHOLDER_TEXT),
    (DEBIT, DEBIT_TEXT),
    (CREDIT, CREDIT_TEXT),
)
