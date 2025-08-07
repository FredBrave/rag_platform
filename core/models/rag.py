from django.db import models
from .usuarios import Usuario

class RAG(models.Model):
    PRIVACIDAD_CHOICES = [
        ("privado", "Privado"),
        ("publico", "Público"),
        ("compartido", "Compartido con usuarios específicos")
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="rags")
    privacidad = models.CharField(max_length=20, choices=PRIVACIDAD_CHOICES, default="privado")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    modelo_llm = models.CharField(max_length=100, default="gpt-4o")
    embedding_model = models.CharField(max_length=100, default="text-embedding-3-small")

    def __str__(self):
        return self.nombre


class RAGPermiso(models.Model):
    rag = models.ForeignKey(RAG, on_delete=models.CASCADE, related_name="permisos")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    puede_editar = models.BooleanField(default=False)

    class Meta:
        unique_together = ("rag", "usuario")

    def __str__(self):
        return f"{self.usuario.username} - {self.rag.nombre}"