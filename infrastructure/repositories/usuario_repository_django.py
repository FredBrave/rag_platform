from typing import Optional
from core.models_domain.usuarios import Usuario
from core.repositories.usuario_repository import UsuarioRepository
from core.models.usuarios import Usuario as UsuarioORM

class UsuarioRepositoryDjango(UsuarioRepository):

    def guardar(self, usuario: Usuario) -> Usuario:
        if usuario.id is not None:
            obj = UsuarioORM.objects.get(id=usuario.id)
            obj.username = usuario.username
            obj.email = usuario.email
            obj.foto_perfil = usuario.foto_perfil_url
            obj.plan = usuario.plan
            obj.save()
        else:
            obj = UsuarioORM.objects.create(
                username=usuario.username,
                email=usuario.email,
                foto_perfil=usuario.foto_perfil_url,
                plan=usuario.plan
            )
            usuario.id = obj.id
        return usuario

    def obtener_por_id(self, usuario_id: int) -> Optional[Usuario]:
        try:
            obj = UsuarioORM.objects.get(id=usuario_id)
            return Usuario(
                id=obj.id,
                username=obj.username,
                email=obj.email,
                foto_perfil_url=obj.foto_perfil.url if obj.foto_perfil else None,
                plan=obj.plan
            )
        except UsuarioORM.DoesNotExist:
            return None

    def obtener_por_username(self, username: str) -> Optional[Usuario]:
        try:
            obj = UsuarioORM.objects.get(username=username)
            return Usuario(
                id=obj.id,
                username=obj.username,
                email=obj.email,
                foto_perfil_url=obj.foto_perfil.url if obj.foto_perfil else None,
                plan=obj.plan
            )
        except UsuarioORM.DoesNotExist:
            return None

    def eliminar(self, usuario_id: int) -> None:
        UsuarioORM.objects.filter(id=usuario_id).delete()