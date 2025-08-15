from rest_framework import serializers

class ConversacionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rag_id = serializers.IntegerField()
    usuario_id = serializers.IntegerField()
    titulo = serializers.CharField()
    fecha_creacion = serializers.DateTimeField()
