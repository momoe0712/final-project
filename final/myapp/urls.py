from django.contrib import admin
from djano.urls import path
from .views import sayHello

urlpatterns = [
    path('', sayHello, name='sayHello'),
]