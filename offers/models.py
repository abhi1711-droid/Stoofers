from django.db import models

from core.models import CreatedUpdatedActive
from static_data.models import City


class Company(CreatedUpdatedActive):
    name = models.CharField(max_length=255)


class Category(CreatedUpdatedActive):
    name = models.CharField(max_length=255)


VALUE_CHOICES = (
    ("FLAT OFF", "FLAT_OFF"),
    ("PERCENT OFF", "PERCENT OFF"),
)


class Offer(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    terms = models.TextField(max_length=5000)
    value = models.FloatField()
    value_type = models.CharField(
        max_length=50, choices=VALUE_CHOICES, default="FLAT OFF"
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Offer_Category(CreatedUpdatedActive):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Offer_City(CreatedUpdatedActive):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
