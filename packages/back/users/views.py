from utils.response import Response
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import UserForm
from ai.models import Ai


@login_required(login_url="/users/login")
def profil(request: HttpRequest) -> JsonResponse:
    user: User = get_object_or_404(User, id=request.user.id)
    if user:
        ais: list[Ai] = user.ais.all()
        return render(request, 'users/profil.html', {'user': user, 'ais': ais})
    return redirect('sign_up')


# def login_user(request: HttpRequest) -> JsonResponse:
#     try:
#         if request.method == "POST":
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = authenticate(request=request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return Response.success("User login successfully!")
#             else:
#                 return Response.error("Bad credential")
#     except Exception as e:
#         return Response.error(e)


def sign_up_user(request: HttpRequest) -> JsonResponse:
    form: UserForm = UserForm(request.data)
    if form.is_valid():
        form.save()
        return Response.success('User created successfully!')
    return Response.error(f'Invalid form data, details: {form.errors}')


@login_required
def logout_user(request: HttpRequest) -> JsonResponse:
    logout(request)
    return Response.success('User logout successfully')
