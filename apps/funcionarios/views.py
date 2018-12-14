from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario

# def home(request):
#     return HttpResponse("Olá")

class FuncionariosList(ListView):
    model = Funcionario
    #ATUALIZANDO A LISTA DE FUNCIONARIO APENAS DA EMPRESA LOGADA,
    #USA O GET_QUERYSET PARA PASSAR O QUE SE QUER
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        # queryset = Funcionario.object.filter(empresa = empresa_logada)
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name_suffix = '_update_form'


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("list_funcionarios")

class FuncionariosNovo(CreateView):
    model = Funcionario
    fields = ["nome", "departamentos"]

    def form_valid(self, form):
        #O COMMIT FALSE É PARA CRIAR UM OBJETO TEMPORARIO, PARA QUE ELE NÃO VÁ PARA O BANCO DE DADOS
        #CRIAR O OBJETO APENAS EM MEMÓRIA E NÃO MANDAR PARA O BANCO
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create_user(username=username,password="ifrn2018")
        funcionario.save()
        return super(FuncionariosNovo, self).form_valid(form)