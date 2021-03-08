from django.contrib import admin
from django.urls import path
from django.urls import path, include
from products.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('favoris/', include('favoris.urls')),
    path('', home, name="home"),
    path('users/', include('django.contrib.auth.urls')),
  
]