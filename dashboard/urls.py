from django.urls import path

from . import views
from authentication import views as auth

urlpatterns = [
    path('', views.index, name='home')
]
