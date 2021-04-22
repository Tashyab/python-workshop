from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="StoreHome"),
    path("about", views.about, name='StoreAbout'),
    path("search", views.search, name='StoreSearch'),
    path("contactus", views.contact, name='StoreContact'),
    path("tracker", views.tracker, name='ProductTracker'),
    path("productview", views.proview, name='ProdView'),
    path("checkout", views.checkout, name='Checkout'),
]