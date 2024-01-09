from django.core.exceptions import ValidationError
from django import forms


def name_characters_only(value):    
    if all(x.isalpha() or x.isspace() for x in value):
        return value
    else:
        raise forms.ValidationError("Please enter valid name")