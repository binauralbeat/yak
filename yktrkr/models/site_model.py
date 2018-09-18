from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import *


class Site(models.Model):
    site_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.site_name}'

    class Meta:
        verbose_name_plural = 'sites'