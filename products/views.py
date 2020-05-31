from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from products.models import Products

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Products.objects.all()[:5] # Nous sélectionnons tous nos articles
    return render(request, 'products/date.html', {'derniers_produits': articles})


def lire(request, id):
    article = get_object_or_404(Products.objects.filter(id_code=id))
    return render(request, 'products/lire.html', {'article':article})