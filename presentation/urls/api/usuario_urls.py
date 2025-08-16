from django.urls import path, include
from infrastructure.views import usuario_views

urlpatterns = [
    path("crear/", usuario_views.CrearUsuarioView, name="crear-usuario"),
    path("<int:usuario_id>/", usuario_views.ObtenerUsuarioPorIdView, name="obtener-usuario-id"),
    path('<int:usuario_id>/api-keys/', include('presentation.urls.api.api_key_urls')),
    path("username/<str:username>/", usuario_views.ObtenerUsuarioPorUsernameView, name="obtener-usuario-username"),
    path("<int:usuario_id>/eliminar/", usuario_views.EliminarUsuarioView, name="eliminar-usuario"),
]