from django.urls import path
from infrastructure.views import documento_views

urlpatterns = [
    path("embeddings/crear/", documento_views.CrearEmbeddingView, name="crear-embedding"),
    path("embeddings/documento/<int:documento_id>/", documento_views.ListarEmbeddingsPorDocumentoView, name="listar-embeddings-documento"),
    path("embeddings/<int:embedding_id>/", documento_views.ObtenerEmbeddingPorIdView, name="obtener-embedding"),
    path("embeddings/documento/<int:documento_id>/eliminar/", documento_views.EliminarEmbeddingsPorDocumentoView, name="eliminar-embeddings-documento"),
]