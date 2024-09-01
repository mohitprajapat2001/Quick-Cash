from tabnanny import verbose
from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.utils.constants import USER_STATUS_TRUE, GENDER_CHOICES
from django_extensions.db.models import ModificationDateTimeField


class Customer(AbstractUser):
    profile = models.ImageField(upload_to="customer_profile", null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=132, null=True, blank=True)
    phone = PhoneNumberField(region="IN", blank=True, null=True)  # type: ignore
    status = models.BooleanField(default=USER_STATUS_TRUE)  # type: ignore
    gender = models.CharField(choices=GENDER_CHOICES, blank=True, null=True)
    modified = ModificationDateTimeField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Banking Customer"
