from rest_framework import serializers

class RAGSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    descripcion = serializers.CharField()
    creador_id = serializers.IntegerField()
    privacidad = serializers.CharField()
    fecha_creacion = serializers.DateTimeField()
    fecha_actualizacion = serializers.DateTimeField()
    modelo_llm = serializers.CharField()
    embedding_model = serializers.CharField()
