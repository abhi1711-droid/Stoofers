from django.db import models

from core.models import CreatedUpdatedActive


class Country(CreatedUpdatedActive):
    name = models.CharField(max_length=255)


class State(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Pincode(CreatedUpdatedActive):
    pincode = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class University(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class College(CreatedUpdatedActive):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
