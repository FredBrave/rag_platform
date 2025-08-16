from rest_framework import serializers

class APIKeySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    usuario_id = serializers.IntegerField(read_only=True)
    proveedor = serializers.CharField(max_length=100)
    clave = serializers.CharField(max_length=255)
    activa = serializers.BooleanField(default=True)
    eliminado = serializers.BooleanField(default=False)
    fecha_creacion = serializers.DateTimeField(read_only=True)
    fecha_actualizacion = serializers.DateTimeField(read_only=True)