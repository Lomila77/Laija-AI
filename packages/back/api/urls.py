from django.urls import path
from . import views

urlpatterns = [
    path("ai/", views.AIListCreate.as_view(), name="list-ai"),
    path("ai/delete/<int:pk>/", views.AIDelete.as_view(), name="delete-ai"),
]
