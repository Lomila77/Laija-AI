from django.urls import path
from .views import get_ais, create

urlpatterns = [
    path('get_ais/', get_ais, name='get_ais'),
    path('create/', create, name='create'),
]
