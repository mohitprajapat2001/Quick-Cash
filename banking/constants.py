from django.utils.translation import gettext as _

# Bank Model Choice Constant
SELECT_PLACEHOLDER = ""
TRANSACTION_CHOICE_PLACEHOLDER_TEXT = "Please Choose Transaction Type"
DEBIT = "DEBIT"
CREDIT = "CREDIT"
TRANSFER = "TRANSFER"
RECEIVE = "RECEIVE"
CREATE = "CREATE"
DEBIT_TEXT = _("Debit")
CREDIT_TEXT = _("Credit")
TRANSFER_TEXT = _("Transfer")
RECEIVE_TEXT = _("Receive")
CREATE_TEXT = _("Create")

# Banking Model Default
BALANCE_DEFAULT = 0

# Model Related Names
BANK_ONE2ONE_CUSTOMER = "bank"
TRANSACTION_FK_CUSTOMER = "transaction"
ACCOUNT_ONE2ONE_CUSTOMER = "account"

# Template Constants

TRANSACTION_TEMPLATE = "banking/transactions.html"
BANKING_TEMPLATE = "banking/banking.html"

# Context Object Name

TRANSACTIONS_CONTEXT_OBJECT_NAME = "transactions"

# Random Account Number
ACCOUNT_NUMBER_START_RANGE = 1000000000
ACCOUNT_NUMBER_END_RANGE = 9999999999

# Transaction Remarks

NEW_ACCOUNT_REMARK = "Account Open with Initial Balance 0"
DEBIT_TRANSACTION_REMARK = "Debit Transaction of Amount ₹ {amount}"
CREDIT_TRANSACTION_REMARK = "Credit Transaction of Amount ₹ {amount}"
TRANSFER_TRANSACTION_REMARK = (
    "Transfer Transaction of Amount {amount} ₹ to {account_number}"
)
RECEIVE_TRANSACTION_REMARK = (
    "Received Transaction of Amount {amount} ₹ from {account_number}"
)
