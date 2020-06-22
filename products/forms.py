from django import forms


class ProductSearch(forms.Form):
    search = forms.CharField(label="", max_length=100,
                             widget=forms.TextInput(attrs={'placeholder':
                                                    "Entrez votre recherche"}))
