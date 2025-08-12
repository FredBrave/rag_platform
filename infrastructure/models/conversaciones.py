from django.db import models
from .rag import RAG
from .usuarios import Usuario

class Conversacion(models.Model):
    rag = models.ForeignKey(RAG, on_delete=models.CASCADE, related_name="conversaciones")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo or f"Conversación con {self.rag.nombre}"

class Mensaje(models.Model):
    ROL_CHOICES = [("usuario", "Usuario"), ("ia", "IA")]

    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name="mensajes")
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.rol}: {self.contenido[:30]}..."