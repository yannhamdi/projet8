from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from products.models import Products

from .forms import ProductSearch

def home(request):
    form = ProductSearch(request.POST or None)
    context = {'form': form}
    return render(request, 'products/home.html', context)

def display(request, id_searched, id_substitue):
    """afficher l'aliment recherché ainsi que l'aliment proposé"""
    product_searched = Products.objects.get(id_code=id_searched)
    product_sub = Products.objects.get(id_code=id_substitue)
    return render(request, 'products/display.html', {'product_searched': product_searched, 'product_sub': product_sub})


def lire(request, id):
    article = get_object_or_404(Products.objects.filter(id_code=id))
    return render(request, 'products/lire.html', {'article':article})


def search(request):
    form = ProductSearch(request.POST or None)
    if form.is_valid():
        prod = form.cleaned_data['search']
        search_sub = Products.objects.search_products(prod)
        if search_sub:
            return redirect(reverse('display', args=[int(search_sub['product_searched']), int(search_sub['substitue'])]))
        return render(request, 'products/no_response.html')
    return render(request, 'products/search.html', locals())



