from django import forms
from .models import Ad

class AdForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    category = forms.ChoiceField(choices=Ad.CATEGORIES)
    short_description = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
