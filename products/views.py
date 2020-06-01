from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from products.models import Products
from .forms import ProductSearch

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Products.objects.all()[:5] # Nous sélectionnons tous nos articles
    return render(request, 'products/date.html', {'derniers_produits': articles})


def lire(request, id):
    article = get_object_or_404(Products.objects.filter(id_code=id))
    return render(request, 'products/lire.html', {'article':article})


def search(request):
    form = ProductSearch(request.POST or None)
    if form.is_valid():
        prod = form.cleaned_data['search']
        prod_id = get_object_or_404(Products.objects.get(food_name__iexact=prod))
        return render(lire(prod_id))
    return render(request, 'products/search.html', locals())

    