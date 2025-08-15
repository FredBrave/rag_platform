from django.urls import path
from infrastructure.views import conversacion_views

urlpatterns = [
    path('crear/', conversacion_views.CrearConversacionView, name='crear-conversacion'),
    path('<int:conversacion_id>/', conversacion_views.ObtenerConversacionView, name='obtener-conversacion'),
    path('usuario/<int:usuario_id>/', conversacion_views.ListarConversacionesUsuarioView, name='listar-conversaciones-usuario'),
    path('<int:conversacion_id>/eliminar/', conversacion_views.EliminarConversacionView, name='eliminar-conversacion'),
]