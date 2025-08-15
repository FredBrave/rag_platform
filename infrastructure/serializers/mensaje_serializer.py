from rest_framework import serializers

class MensajeSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    conversacion_id = serializers.IntegerField()
    rol = serializers.CharField()
    contenido = serializers.CharField()
    fecha = serializers.DateTimeField()