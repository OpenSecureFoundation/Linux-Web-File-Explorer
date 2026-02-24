from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # La racine de l'app
]