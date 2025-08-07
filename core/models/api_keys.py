from django.db import models
from .usuarios import Usuario

class APIKey(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="api_keys")
    proveedor = models.CharField(max_length=50, choices=[("openai", "OpenAI"), ("anthropic", "Anthropic")])
    clave = models.CharField(max_length=200)
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.proveedor} - {self.usuario.username}"