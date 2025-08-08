from django.db import models
from .documentos import Documento

class Embedding(models.Model):
    documento = models.ForeignKey(
        Documento,
        on_delete=models.CASCADE,
        related_name="embeddings"
    )
    texto_fragmento = models.TextField(help_text="Fragmento original del documento")
    vector = models.JSONField(help_text="Vector de embedding del fragmento")
    indice = models.PositiveIntegerField(help_text="Posición del fragmento en el documento")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["indice"]
        indexes = [
            models.Index(fields=["indice"]),
            models.Index(fields=["documento"]),
        ]

    def __str__(self):
        return f"Embedding {self.indice} - {self.documento.titulo}"