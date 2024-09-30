from atexit import register
from django.template import Library

register = Library()


@register.filter(name="check_nagative")
def check_negative(*args):
    if args < 0:
        return False
    else:
        return True
