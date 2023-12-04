from django import forms
from .models import *

PRODUCT_CATEGORY = Category.objects.all()


class AddProduct(forms.Form):
    name = forms.CharField(max_length=60)
    price = forms.IntegerField()
    photo = forms.ImageField()
    description = forms.CharField()
    category = forms.ModelChoiceField(queryset=PRODUCT_CATEGORY)
