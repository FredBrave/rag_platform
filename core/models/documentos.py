from django.db import models
from .rag import RAG

class Documento(models.Model):
    rag = models.ForeignKey(RAG, on_delete=models.CASCADE, related_name="documentos")
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to="rags/documentos/")
    texto_extraido = models.TextField(blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    