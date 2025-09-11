from django.views.generic import FormView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Endereco
from .forms import EnderecoForm
import requests

class EnderecoCreateView(FormView):
    template_name = 'form.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/', verify=False)
        data = response.json()

        if 'erro' not in data:
            Endereco.objects.create(
                rua=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                cidade=data.get('localidade', ''),
                estado=data.get('uf', ''),
                cep=cep
            )
        return super().form_valid(form)

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'list.html'
    context_object_name = 'enderecos'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'detail.html'
    context_object_name = 'endereco'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')
