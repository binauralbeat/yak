from django.contrib.auth.models import User
from django import forms
from website.models import Product
from website.models import Category
from website.models import CustomerRegistration

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class CustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerRegistration
        fields = ['street', 'city', 'state', 'zip', 'phone_number']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ["user"]
        fields = ['title', 'description', 'price', 'quantity', 'date_added',
'location', 'local_delivery', 'category_name', 'image']


# class CategoryForm(forms.ModelForm):
#     '''
#     Category Form
#     Author: Deanna Vickers
#     Purpose: Create form on website app to add categories
#     '''

#     class Meta:
#         model = Category
#         fields = ('name',)