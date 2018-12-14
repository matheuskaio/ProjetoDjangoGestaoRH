from django.urls import path
from .views import DocumentoCreate
    # DocumentoList, DocumentoUpdate, DocumentoDelete
urlpatterns = [
    path("novo/<int:funcionario_id>/", DocumentoCreate.as_view(), name="create_documentos")
    # path("list/", DocumentoList.as_view(), name="list_documentos"),
    # path("update/<int:pk>/", DocumentoUpdate.as_view(), name="update_documentos"),
    # path("delete/<int:pk>/", DocumentoDelete.as_view(), name="deletar_documentos"),
]

