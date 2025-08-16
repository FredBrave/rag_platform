from rest_framework import serializers

class DocumentoSerializer(serializers.Serializer):
    rag = serializers.IntegerField(required=False)
    nombre = serializers.CharField(max_length=200)
    archivo = serializers.FileField()
    texto_extraido = serializers.CharField(required=False, allow_blank=True)
    fecha_subida = serializers.DateTimeField(required=False)
