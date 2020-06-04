
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from products import views
from favoris import views
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('favoris/', include('favoris.urls')),
]
