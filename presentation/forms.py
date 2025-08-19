from django import forms
from infrastructure.models.rag import RAG
from infrastructure.models.conversaciones import Conversacion
from infrastructure.models.documentos import Documento

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


class ConversacionForm(forms.ModelForm):
    class Meta:
        model = Conversacion
        fields = ["titulo"]

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ["nombre", "archivo"]
        
