from django.core.exceptions import ValidationError
from accounts.utils.constants import PASSWORD_RE_PATTERN
from django.utils.translation import gettext as _
import re


def password_validator(value):
    if not re.match(PASSWORD_RE_PATTERN):
        raise ValidationError(_("Please Match Required Password Format"))
    return value
