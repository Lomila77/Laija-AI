from utils.response import Response
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
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

def sign_up(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        form: UserForm = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return Response.success('User created successfully!')
        return Response.error('Invalid form data')
    form: UserForm = UserForm()
    return render(request, 'users/sign_up.html', {'form': form})

@login_required
def logout(request: HttpRequest) -> HttpResponseRedirect:
    django_logout(request)
    return redirect('login')
