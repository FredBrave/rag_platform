from rest_framework import serializers

class EmbeddingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    documento_id = serializers.IntegerField()
    texto_fragmento = serializers.CharField()
    vector = serializers.ListField(
        child=serializers.FloatField(),
        help_text="Vector numérico del embedding"
    )
    indice = serializers.IntegerField()
    creado_en = serializers.DateTimeField(read_only=True)