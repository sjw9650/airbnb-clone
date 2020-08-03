from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

GENDER_MALE = "male"
GENDER_FEMALE = "female"
GENDER_OTHER = "ohter"

GENDER_CHOICES = (
    (GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
    (GENDER_OTHER, "Other"),
)

LANGUAGE_ENGLISH = "english"
LANGUAGE_KOREAN = "korean"

LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))


CURRENCY_ENGLISH = "usd"
CURRENCY_KOREAN = "krw"

CURRENCY_CHOICES = ((CURRENCY_ENGLISH, "USD"), (CURRENCY_KOREAN, "KRW"))


class User(AbstractUser):
    """ Custom User mode """

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )

    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )

    superhost = models.BooleanField(default=False)

