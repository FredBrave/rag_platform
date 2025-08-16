from rest_framework import serializers

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=100)
    foto_perfil = serializers.CharField(max_length=255, allow_blank=True, required=False)
    plan = serializers.ChoiceField(choices=[("free", "Free"), ("pro", "Pro")], default="free")
    password = serializers.CharField(write_only=True, min_length=6)