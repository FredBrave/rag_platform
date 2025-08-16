from django.urls import path, include
from infrastructure.views import rag_views

urlpatterns = [
    path("crear/", rag_views.crear_rag_view, name="crear_rag"),
    path("<int:rag_id>/", rag_views.obtener_rag_por_id_view, name="obtener_rag"),
    path('<int:rag_id>/conversaciones/', include('presentation.urls.api.conversacion_urls')),
    path('<int:rag_id>/documentos/', include('presentation.urls.api.documento_urls')),
    path("<int:rag_id>/permiso/crear/", rag_views.crear_permiso_rag_view, name="crear_rag_permiso"),
    path("<int:rag_id>/permisos/", rag_views.obtener_permisos_por_rag_view, name="ver_rag_permisos"),
    path("<int:rag_id>/puede_editar/", rag_views.puede_editar_rag_view, name="puede_editar_rag"),
    path("usuario/<int:creador_id>/", rag_views.listar_rags_por_usuario_view, name="listar_rags_usuario"),
    path("<int:rag_id>/eliminar/", rag_views.eliminar_rag_view, name="eliminar_rag"),
    path("<int:rag_permiso_id>/eliminar_rag_permiso/", rag_views.eliminar_rag_permiso_view, name="eliminar_rag_permiso"),
]