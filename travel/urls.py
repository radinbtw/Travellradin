from django.contrib import admin
from django.urls import path, include

from travel.views import travello, create_travel

urlpatterns = [
    path('travell/',travello),
    path('create/',create_travel,name='create_travel')
]