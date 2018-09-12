from django.db import models
from django.db.models import *


class Site(models.Model):



    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'sites'