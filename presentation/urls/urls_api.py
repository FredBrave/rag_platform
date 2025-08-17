from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rags/', include('presentation.urls.api.rag_urls')),
    path('usuario/', include('presentation.urls.api.usuario_urls')),
]
