from django.urls import path, reverse, include
from . import views

urlpatterns = [
path('signup/', views.signup, name="signup"),
path('products/', include('products.urls')),
]