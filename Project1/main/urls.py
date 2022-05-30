from unicodedata import name
from django import views
from django.urls import path, include   
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('about Galymzhan', views.aboutG, name='aboutG'),
    path('about Ali', views.aboutA, name='aboutA'),
    path('about Yerkebulan', views.aboutY, name='aboutY'),
    path('history', views.history, name='hist'),
    path('traditions', views.trad, name='trad'),
    path('insert', views.insert, name='insert'),#creat puth of insert
    path('update/<int:pk>/', views.update, name='update'),#creat puth of update
    path('delete/<int:pk>/', views.delete, name='delete'),#creat puth of delete
    path('details/<slug:slug>/', views.details, name='details'),
    path('nature', views.nature, name='nat'),
    path('megapolises', views.megap, name='megap'),
    path('reg/', views.reg, name='reg'),
    path('send/', views.send_message),
    path('pres', views.pres, name="pres"),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
]
