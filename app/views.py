from typing import Any
from django.shortcuts import render
from app.models import Funcionario
from django.views.generic import DetailView, TemplateView
from app.forms import ContactForm
from django.http import HttpResponseRedirect
from app.models import Funcionario


class PublisherDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    def get_queryset(self):
        funcionario_id = self.kwargs['pk']

        # Filtra os funcionários pelo ID fornecido na URL
        return Funcionario.objects.filter(id=funcionario_id)





class AuthorCreateView(TemplateView):
    form_class = ContactForm
   

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,'author_form.html',{'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            form.save(commit=True)
            funcionario = Funcionario.objects.all().order_by('-id')[0]
            
            return HttpResponseRedirect(f"/funcionario/{funcionario.id}")

