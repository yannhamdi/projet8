from django.urls import path, reverse, include
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
path('signup/', views.signup, name="signup"),
path('products/', include('products.urls')),
path('signin/', views.signin, name="signin"),
 path('account/', views.account, name="account"),
path("signout/", LogoutView.as_view(), name="signout"),
]