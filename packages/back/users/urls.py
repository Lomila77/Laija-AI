from django.urls import path
from .views import profil, sign_up, logout
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('profil/', profil, name='profil'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]
