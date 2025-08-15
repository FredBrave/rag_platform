from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rags/', include('presentation.urls.api.rag_urls')),
    path('conversaciones/', include('presentation.urls.api.conversacion_urls')),
]
