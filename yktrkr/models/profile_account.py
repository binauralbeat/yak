from django.contrib.auth.models import User
from django.db import models
from django.db.models import *



class CustomerRegistration(models.Model):
	'''
	Author: Meghan Debity
	Purpose: Model for buying and selling user(s)
	'''
	street = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=10)
	zip = models.IntegerField()
	phone_number = models.IntegerField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.username

	class Meta:
		db_table = "customer"