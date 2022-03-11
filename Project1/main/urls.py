from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about'),
    path('history', views.history, name='hist'),
    path('traditions', views.trad, name='trad'),
    path('nature', views.nature, name='nat'),
    path('megapolises', views.megap, name='megap'),
]
