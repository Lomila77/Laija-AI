from utils.response import Response
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import User
from .forms import UserForm
from ai.models import Ai


@login_required
def profil(request: HttpRequest) -> JsonResponse:
    user: User = get_object_or_404(User, id=request.user.id)
    if user:
        ais: list[Ai] = user.ais.all()
        return render(request, 'users/profil.html', {'user': user, 'ais': ais})
    return redirect('sign_up')

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def sign_up(request: HttpRequest) -> JsonResponse:
    form: UserForm = UserForm(request.data)
    if form.is_valid():
        form.save()
        return Response.success('User created successfully!')
    return Response.error(f'Invalid form data, details: {form.errors}')

@login_required
def logout(request: HttpRequest) -> JsonResponse:
    django_logout(request)
    return Response.success('User logout successfully')
