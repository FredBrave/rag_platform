from rest_framework import serializers
from core.models_domain.rag import RAG

class RAGSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length=255)
    descripcion = serializers.CharField()
    privado = serializers.BooleanField()
    usuario_id = serializers.IntegerField()

    def create(self, validated_data):
        return RAG(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get("nombre", instance.nombre)
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.privado = validated_data.get("privado", instance.privado)
        return instance