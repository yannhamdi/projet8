from django.urls import path, reverse, include
from . import views
from django.conf import settings

urlpatterns = [
path('signup/', views.signup, name="signup"),
path('products/', include('products.urls')),
path('signin/', views.signin, name="signin"),
 path('account/', views.account, name="account"),
path("signout/", views.signout, name="signout"),
path("change_password/", views.change_password, name="change_password"),
]