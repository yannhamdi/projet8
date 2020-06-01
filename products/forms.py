from django import forms


class ProductSearch(forms.Form):
    search = forms.CharField(max_length=100)