from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from products.models import Products
from .forms import ProductSearch

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Products.objects.all() # we select all products
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/date.html', {'page_obj': page_obj})


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
        cat = category_product[0]
        better_product = Products.objects.filter(category=cat).filter(nutrition_grade__lt=produ_id[0].nutrition_grade)
        return redirect(reverse('lire', args=[better_product[0].id_code]))
    return render(request, 'products/search.html', locals())

    