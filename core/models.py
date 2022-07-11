from django.db import models

# Create your models here.

from django.db import models


class CreatedUpdatedActive(models.Model):  # COMM0N
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
