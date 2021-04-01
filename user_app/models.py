from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """ A model for presenting User"""

    average_mark = models.DecimalField(max_digits=3, decimal_places=2)
