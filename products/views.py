from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from random import randint
from products.models import Products
from .forms import ProductSearch


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
        produ_id = Products.objects.filter(food_name__icontains=prod)
        category_product = produ_id[0].category.all()
        if len(category_product) > 1:
            cat = category_product[0]
            better_product = Products.objects.filter(category=cat).filter(nutrition_grade__lt=produ_id[0].nutrition_grade)
            i=(len(better_product))-1
            j=randint(0,i)
        cat = category_product[0]
        better_product = Products.objects.filter(category=cat).filter(nutrition_grade__lt=produ_id[0].nutrition_grade)
        i=(len(better_product))-1
        j=randint(0,i)
        return redirect(reverse('display', args=[int(produ_id[0].id_code), int(better_product[j].id_code)]))
    return render(request, 'products/search.html', locals())



