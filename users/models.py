import random
import string

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from core.models import CreatedUpdatedActive
from static_data.models import College

current_user = get_user_model()


class CustomUserModel(CreatedUpdatedActive):
    phone = models.CharField(null=True, unique=True, max_length=10)
    pincode = models.CharField(max_length=6)
    college = models.CharField(null=True, max_length=100)
    user = models.ForeignKey(current_user, on_delete=models.CASCADE, unique=True)
    objects = models.Manager()


prefix_list = [
    "8010",
    "8011",
    "8012",
    "8013",
    "8014",
    "7010",
    "7011",
    "7012",
    "7013",
    "7014",
]


def generate_card():
    new_link = "".join(random.choices(string.digits, k=6))
    return random.choice(prefix_list) + new_link


class StoofersCard(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=10, unique=True, default=generate_card)
    user = models.ForeignKey(current_user, on_delete=models.CASCADE, unique=True)
    objects = models.Manager()
