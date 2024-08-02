from django.urls import path
from .views import profil, sign_up, logout
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('profil/', profil, name='profil'),
    path('sign-up/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
