from django.urls import path, reverse
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('home/', TemplateView.as_view(template_name="products/home.html"), name='home'),
    path('article/<int:id>', views.lire, name='lire'),
    path('search/', views.search, name='search'),
    path('display/<int:id_searched>/<int:id_substitue>', views.display, name='display')


]