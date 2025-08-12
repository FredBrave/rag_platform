from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Puedes agregar más atributos si quieres
    foto_perfil = models.ImageField(upload_to="usuarios/perfiles/", blank=True, null=True)
    plan = models.CharField(max_length=20, choices=[("free", "Free"), ("pro", "Pro")], default="free")


    def __str__(self):
        return self.username