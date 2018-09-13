from django.contrib.auth.models import User
from django import forms
# from website.models import Product
# from website.models import Category
from yktrkr.models import CustomerRegistration


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerRegistration
        fields = ['street', 'city', 'state', 'zip', 'phone_number']






class SearchForm(forms.Form):

	"""
	Author: Meghan Debity
	Purpose: Create form model for product search feature
	"""

	search_bar = forms.CharField(max_length = 25)

