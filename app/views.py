from django.shortcuts import render
from app.models import Funcionario
from django.views.generic import DetailView

class PublisherDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    def get_queryset(self):
        funcionario_id = self.kwargs['pk']

        # Filtra os funcionários pelo ID fornecido na URL
        return Funcionario.objects.filter(id=funcionario_id)
