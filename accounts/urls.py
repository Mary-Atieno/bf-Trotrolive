from django.urls import path
from . import views

urlpatterns = [
    # path('',views.base, name='base'),
    path('',views.home, name='index'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('geocode',views.geocode, name='geocode'),


]