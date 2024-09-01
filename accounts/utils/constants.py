from django.utils.translation import gettext_lazy as _

# Accounts Models Constants
USER_STATUS_TRUE = 1
USER_STATUS_FALSE = 0

# Regular Expression Constants
PASSWORD_RE_PATTERN = (
    "((?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)\w.{6,18}\w)"  # type: ignore
)

# Customer Model Choice
MALE = _("MALE")
MALE_TEXT = _("Male")
FEMALE = _("FEMALE")
FEMALE_TEXT = _("Female")
SELECT_GENDER = _("SELECT")

GENDER_CHOICES = ((MALE, MALE_TEXT), (FEMALE, FEMALE_TEXT))
GENDER_CHOICES_FORM = ((MALE, MALE_TEXT), (FEMALE, FEMALE_TEXT))

# Status Constants
STATUS_INACTIVE_BOOL = False
STATUS_ACTIVE_BOOL = True

# Descriptions
CUSTOMER_ADMIN_STATUS_UNACTIVE_DESCRIPTION = "Mark Selected Customers Unactive"
CUSTOMER_ADMIN_STATUS_ACTIVE_DESCRIPTION = "Mark Selected Customers Active"

# Template Constants
PROFILE_TEMPLATE = "accounts/profile.html"
LOGIN_TEMPLATE = "accounts/login.html"
REGISTER_TEMPLATE = "accounts/register.html"

# Messages
PROFILE_UPDATE_SUCCESS = "User Profile Updated Successfully"
LOGOUT_SUCCESS = "User Logged out Successfully"
LOGIN_SUCCESS = "User Logged in Successfully"
LOGIN_ERROR = "Try Again, Username or Password is Incorrect Please Check Credentials"
SIGNUP_SUCCESS = "User registered successfully"
PASSWORD_NOT_MATCH = "Try again, Password not match"
TERMS_NOT_CHECKED = "PLease Agree Terms & Conditions"

# Profile Form Variables
PROFILE_FORM_PLACEHOLDER = {
    "profile": "Place Update Profile Picture",
    "first_name": "Place Select First Name",
    "last_name": "Place Select Last name",
    "email": "Place Enter Email",
    "age": "Place Choose Age",
    "gender": "Place Choose Gender",
    "phone": "Place Add Contact Details",
    "address": "Place Update Address",
}
LOGIN_FORM_PLACEHOLDER = {
    "username": "Please Enter Login Username",
    "password": "Please Enter Password",
}
SIGNUP_FORM_PLACEHOLDER = {
    "first_name": "Please Enter First Name",
    "last_name": "Please Enter Last Name",
    "username": "Please Choose Username",
}
SIGN_UP_USERNAME_HELP_TEXT = "Username is Required Field"

# Form Class
FORM_CLASS_BASIC = "form-control p-2 border"

# URLS
DASHBOARD_REVERSE = "dashboard"
DASHBOARD_URL = "/dashboard/"
LOGIN_REVERSE = "login"
