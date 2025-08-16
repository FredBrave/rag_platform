from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from infrastructure.serializers.documento_serializer import DocumentoSerializer
from core.use_cases.documento_case_uses import CrearDocumento, ObtenerDocumento, ListarDocumentos, EliminarDocumento
from infrastructure.repositories.documento_repository_django import DocumentoRepositoryDjango
import os
from django.conf import settings
from PyPDF2 import PdfReader


@api_view(["POST"])
def crear_documento(request, rag_id):
    serializer = DocumentoSerializer(data=request.data)
    if serializer.is_valid():
        nombre = serializer.validated_data["nombre"]
        archivo = serializer.validated_data["archivo"]

        folder_path = os.path.join(settings.MEDIA_ROOT, "rags", str(rag_id), "documentos")
        os.makedirs(folder_path, exist_ok=True)

        save_path = os.path.join(folder_path, archivo.name)

        with open(save_path, "wb+") as f:
            for chunk in archivo.chunks():
                f.write(chunk)

        relative_path = os.path.join("rags", str(rag_id), "documentos", archivo.name)

        use_case = CrearDocumento(DocumentoRepositoryDjango())
        documento = use_case.execute(
            rag_id=rag_id,
            nombre=nombre,
            archivo=relative_path
        )

        return Response({
            "id": documento.id,
            "nombre": documento.nombre,
            "archivo": relative_path
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def obtener_documento(request, documento_id, rag_id):
    use_case = ObtenerDocumento(DocumentoRepositoryDjango())
    documento = use_case.execute(documento_id)

    if not documento:
        return Response({"error": "Documento no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        "id": documento.id,
        "nombre": documento.nombre,
        "rag_id": documento.rag_id
    })


@api_view(["GET"])
def listar_documentos(request, rag_id):
    """
    Listar todos los documentos.
    """
    use_case = ListarDocumentos(DocumentoRepositoryDjango())
    documentos = use_case.execute()

    return Response([
        {
            "id": d.id,
            "rag_id": d.rag_id,
            "nombre": d.nombre
        } for d in documentos
    ])


@api_view(["DELETE"])
def eliminar_documento(request, documento_id):
    use_case = EliminarDocumento(DocumentoRepositoryDjango())
    use_case.execute(documento_id)

    return Response({"mensaje": "Documento eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
