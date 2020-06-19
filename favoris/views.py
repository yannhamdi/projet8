from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from products.models import Products
from products.forms import ProductSearch
from users.models import User
from favoris.models import Favorite



@login_required
def saving_search(request,id_searched, id_substitue):
    """views to save the user's search"""
    product = Products.objects.get(id_code=id_searched)
    sub = Products.objects.get(id_code=id_substitue)
    Favorite.objects.get_or_create(user_link=request.user, product_searched=product, product_substitute=sub)
    return redirect('home')



@login_required
def display_account(request):
    """views that display searched details"""
    favoris = Favorite.objects.filter(user_link=request.user).order_by('product_searched')
    paginator = Paginator(favoris, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'display_account.html', {'page_obj': page_obj})