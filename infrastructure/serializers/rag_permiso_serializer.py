from rest_framework import serializers

class RagPermisoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    rag_id = serializers.IntegerField()
    usuario_id = serializers.IntegerField()
    puede_editar = serializers.BooleanField()
