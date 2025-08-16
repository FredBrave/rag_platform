from django.urls import path
from infrastructure.views import api_key_views

urlpatterns = [
    path("crear/", api_key_views.CrearAPIKeyView, name="crear_api_key"),
    path("<int:api_key_id>/", api_key_views.ObtenerAPIKeyView, name="obtener_api_key"),
    path("usuario/<int:usuario_id>/", api_key_views.ListarAPIKeysUsuarioView, name="listar_api_keys_usuario"),
    path("<int:api_key_id>/desactivar/", api_key_views.DesactivarAPIKeyView, name="desactivar_api_key"),
    path("<int:api_key_id>/eliminar/", api_key_views.EliminarAPIKeyView, name="eliminar_api_key"),
]