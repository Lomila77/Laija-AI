from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from utils.response import Response
from .models import Ai
from .forms import AiForm

@login_required
def get_ais(request: HttpRequest) -> JsonResponse:
    ais = get_list_or_404(Ai, user_id=request.user.id)
    if ais:
        return render(request, 'ai/profil.html', {'ais': ais})
    return Response.success('Ai retrieved successfully!')

@login_required
def create(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        form = AiForm(request.POST)
        if form.is_valid():
            ai = form.save(commit=False)
            ai.user_id = request.user.id
            ai.save()
            return Response.success('Ai created successfully!')
        return Response.error('Invalid form data')
    form = AiForm()
    return render(request, 'ai/create.html', {'form': form})
