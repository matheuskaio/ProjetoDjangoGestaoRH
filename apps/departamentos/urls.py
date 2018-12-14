from django.urls import path
from .views import DepartamentoCreate, DepatamentoUpdate, DepatamentoList, DepatamentoDelete
urlpatterns = [
    path("novo/", DepartamentoCreate.as_view(), name="create_departamentos"),
    path("list/", DepatamentoList.as_view(), name="list_departamentos"),
    path("update/<int:pk>/", DepatamentoUpdate.as_view(), name="update_departamentos"),
    path("delete/<int:pk>/", DepatamentoDelete.as_view(), name="deletar_departamento"),
]

