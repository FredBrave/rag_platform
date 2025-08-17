from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from core.use_cases.rag_case_uses import ListarRAGsPorPrivacidad

@login_required
def home(request):
    listar_rags = ListarRAGsPorPrivacidad(RagRepositoryDjango())
    public_rags = listar_rags.execute(privacidad="publico")

    context = {
        'public_rags': public_rags,
    }
    return render(request, 'home.html', context)