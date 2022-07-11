import random
import string

from django.db import models
from django.contrib.auth import get_user_model

from core.models import CreatedUpdatedActive
from static_data.models import College

User = get_user_model()


class CustomUserModel(CreatedUpdatedActive):
    phone = models.CharField(null=True, unique=True, max_length=10)
    pincode = models.CharField(max_length=6)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


Get_User = get_user_model()

prefix_list = [
    "94518010",
    "94518011",
    "94158010",
    "94158011",
    "94157010",
    "94157011",
    "94517010",
    "94517011",
]


def generate_card():
    new_link = "".join(random.choices(string.digits, k=8))
    return random.choice(prefix_list) + new_link


class StoofersCard(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16, unique=True, default=generate_card)
    user = models.ForeignKey(Get_User, on_delete=models.CASCADE, default=-1)
