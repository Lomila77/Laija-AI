from django.urls import path
from .views import profil, sign_up_user, logout_user
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('profil/', profil, name='profil'),
    path('sign-up/', sign_up_user, name='sign_up'),
    path('logout/', logout_user, name='logout'),
    path("login/", auth_views.LoginView.as_view()),
    #path('login/', TokenObtainPairView.as_view(), name='login'),
    #path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
