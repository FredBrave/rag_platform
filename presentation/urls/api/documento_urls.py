from django.urls import path
from infrastructure.views import documento_views

urlpatterns = [
    path("", documento_views.listar_documentos, name="listar_documentos"),
    path("crear/", documento_views.crear_documento, name="crear_documento"),
    path("<str:documento_id>/", documento_views.obtener_documento, name="obtener_documento"),
    path("<str:documento_id>/eliminar/", documento_views.eliminar_documento, name="eliminar_documento"),
]