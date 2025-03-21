from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AISerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AI


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AIListCreate(generics.ListCreateAPIView):
    serializer_class = AISerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return AI.objects.filter(creator=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(creator=self.request.user)
        print(serializer.errors)


class AIDelete(generics.DestroyAPIView):
    serializer_class = AISerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return AI.objects.filter(creator=user)

