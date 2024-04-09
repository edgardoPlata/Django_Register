from django.urls import path, include
from .views import home, products, exit
urlpatterns = [
    path('',home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit')
]
