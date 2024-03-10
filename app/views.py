from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from app.models import Funcionario
from django.views.generic import CreateView, ListView,DeleteView, UpdateView,TemplateView, DetailView
from app.forms import ContactForm
from django.http import  HttpResponseRedirect
from app.models import Funcionario
from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth import user_logged_in
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import user_logged_in
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

def logout_view(request):
    logout(request)
    return redirect("login")

User = get_user_model()


class LoginUsuario(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()


        error_messages = {
            'invalid_login': gettext_lazy('Verifique o usuario e senha e tente novamente.'),
            'inactive': gettext_lazy("Usuario inativo."),
        }
        
        AuthenticationForm.error_messages = error_messages

        return super().form_invalid(form)

class ListFuncionarios(ListView):
    model = Funcionario

    template_name = 'funcionario_list.html'
    def get(self, request):
        user = self.request.user
        user = self.request.user
        autenticado = user.is_authenticated
        if autenticado:
            lista = Funcionario.objects.filter(usuario=user)
        else:
            lista = ''
        return render(request, self.template_name,{"page_obj":lista,"autenticado":autenticado})
    
class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    def get_queryset(self):
        user = self.request.user

        funcionario_id = self.kwargs['pk']
        return Funcionario.objects.filter(id=funcionario_id,usuario=user)


class AuthorCreateView(TemplateView):
    form_class = ContactForm
   
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated
        lista = Funcionario.objects.filter(usuario=user)
        print(f"##############{user}#################")
        return render(request,'funcionario_create.html',{'form':form,'autenticado':autenticado,'funcionarios':lista})


    def post(self, request):
        form = self.form_class(request.POST)
        
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.usuario = self.request.user
            # funcionario = Funcionario.objects.all().order_by('-id')[0]
            funcionario.save()
            return HttpResponseRedirect(f"/create-funci/")

