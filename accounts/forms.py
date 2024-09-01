from django.forms import (
    EmailInput,
    ModelForm,
    ClearableFileInput,
    NumberInput,
    PasswordInput,
    TextInput,
    Select,
    Form,
    CharField,
)
from accounts.models import Customer
from accounts.utils.constants import (
    PROFILE_FORM_PLACEHOLDER,
    LOGIN_FORM_PLACEHOLDER,
    FORM_CLASS_BASIC,
    SIGNUP_FORM_PLACEHOLDER,
    SIGN_UP_USERNAME_HELP_TEXT,
)


class CustomerUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            "profile",
            "first_name",
            "last_name",
            "email",
            "age",
            "gender",
            "phone",
            "address",
        ]
        widgets = {}
        for field in fields:
            input_option = TextInput

            if field == "profile":
                input_option = ClearableFileInput
            elif field == "age" or field == "phone":
                input_option = NumberInput
            elif field == "email":
                input_option = EmailInput
            elif field == "gender":
                input_option = Select
            widgets[field] = input_option(
                attrs={
                    "class": FORM_CLASS_BASIC,
                    "placeholder": PROFILE_FORM_PLACEHOLDER[field],
                }
            )


class LoginForm(Form):
    username = CharField(
        required=True,
        widget=TextInput(
            attrs={
                "class": FORM_CLASS_BASIC,
                "plcaeholder": LOGIN_FORM_PLACEHOLDER.get("username"),
            }
        ),
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": FORM_CLASS_BASIC,
                "plcaeholder": LOGIN_FORM_PLACEHOLDER.get("password"),
            }
        ),
    )


class RegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "username",
        ]
        widgets = {}
        help_text = {}
        labels = {}
        for field in fields:
            widgets[field] = TextInput(
                attrs={
                    "class": FORM_CLASS_BASIC,
                    "required": True if field == "username" else False,
                }
            )
            labels[field] = SIGNUP_FORM_PLACEHOLDER[field]
            if field == "username":
                help_text[field] = SIGN_UP_USERNAME_HELP_TEXT
