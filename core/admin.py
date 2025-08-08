from django.contrib import admin
from .models.usuarios import Usuario
from .models.rag import RAG, RAGPermiso
from .models.embedding import Embedding
from .models.documentos import Documento
from .models.conversaciones import Conversacion, Mensaje
from .models.api_keys import APIKey



admin.site.register(Usuario)
admin.site.register(RAG)
admin.site.register(RAGPermiso)
admin.site.register(Embedding)
admin.site.register(Documento)
admin.site.register(Conversacion)
admin.site.register(Mensaje)
admin.site.register(APIKey)