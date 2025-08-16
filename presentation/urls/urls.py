from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rags/', include('presentation.urls.api.rag_urls')),
]
