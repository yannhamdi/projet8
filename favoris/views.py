from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from products.models import Products
from products.forms import ProductSearch
from users.models import User
from favoris.models import Favorite


