from django.urls import path, include
from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionariosNovo

urlpatterns = [
    # path('', home, name='page_home_funcionario'),
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionariosNovo.as_view(), name='create_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario')
]