from django.urls import path, reverse
from . import views

urlpatterns = [
path('signup/', views.signup, name="signup")
]