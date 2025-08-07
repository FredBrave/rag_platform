from django.db import models
from .documentos import Documento

class Embedding(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name="embeddings")
    texto_fragmento = models.TextField()
    vector = models.JSONField()
    indice = models.IntegerField()

    def __str__(self):
        return f"Embedding {self.indice} de {self.documento.nombre}"