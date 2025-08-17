from django import forms
from django import forms
from infrastructure.models.rag import RAG

class RAGForm(forms.ModelForm):
    class Meta:
        model = RAG
        fields = ["nombre", "descripcion", "privacidad", "modelo_llm", "embedding_model"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
        }

class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, label="Usuario")
    email = forms.EmailField(label="Correo")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
