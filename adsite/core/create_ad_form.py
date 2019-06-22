from django import forms
from .models import Ad

class AdForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    category = forms.ChoiceField(choices=Ad.CATEGORIES)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()

    def clean_ad(self):
        """Get data from the form and return ad"""
        cleaned_data = super(AdForm, self).clean()
        ad = Ad()
        ad.title = cleaned_data['title']
        ad.description = cleaned_data['description']
        ad.category = cleaned_data['category']
        ad.price = cleaned_data['price']
        return ad