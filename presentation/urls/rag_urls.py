from django.urls import path
from infrastructure.views import rag_views

urlpatterns = [
    path("rags/crear/", rag_views.crear_rag_view, name="crear_rag"),
    path("rags/<int:rag_id>/", rag_views.obtener_rag_por_id_view, name="obtener_rag"),
    path("rags/usuario/<int:usuario_id>/", rag_views.listar_rags_por_usuario_view, name="listar_rags_usuario"),
    path("rags/<int:rag_id>/eliminar/", rag_views.eliminar_rag_view, name="eliminar_rag"),
]