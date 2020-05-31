from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Products.objects.all()[:5] # Nous sélectionnons tous nos articles
    return render(request, 'products/date.html', {'derniers_produits': articles})

