from django import forms
from .models import Book

from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[0-9]{13}$', 'Must be 13 digits with no hyphens')

class WhatBookForm(forms.Form):
    ISBN_number = forms.CharField(label = 'Book-ISBN-Number', widget = forms.TextInput(), validators=[numeric])
