from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from infrastructure.repositories.rag_repository_django import RagRepositoryDjango
from core.use_cases.rag_case_uses import ListarRAGsPorPrivacidad, ListarRAGsPorUsuario

@login_required(login_url='login')
def home(request):
    listar_rags = ListarRAGsPorPrivacidad(RagRepositoryDjango())
    public_rags = listar_rags.execute(privacidad="publico")

    context = {
        'public_rags': public_rags,
    }
    return render(request, 'home.html', context)


@login_required
def mis_rags(request):
    listar_rags = ListarRAGsPorUsuario(RagRepositoryDjango())

    user_rags = listar_rags.execute(request.user.id)
    
    context = {
        "user_rags": user_rags
    }
    return render(request, "rags/mis_rags.html", context)