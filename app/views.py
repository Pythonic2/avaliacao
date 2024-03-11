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
from .forms import SignUpForm,NovoFunciForm
from django.contrib.auth.mixins import LoginRequiredMixin



def logout_view(request):
    logout(request)
    return redirect("login")

User = get_user_model()




class RegisterUser(TemplateView):

    def get(self, request):
        msg = None
        success = False
        form = SignUpForm()
        return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


    def post(self,request):
        msg = None
        success = False

        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=username, password=raw_password)

                msg = 'User created - please <a href="/login">login</a>.'
                success = True

                return redirect("/")

            else:
                msg = 'Form is not valid'
    

class LoginUsuario(LoginView):
    template_name = 'accounts/login.html'

    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        user_exists = User.objects.filter(username=username).exists()


        error_messages = {
            'invalid_login': gettext_lazy('Verifique o usuario e senha e tente novamente.'),
            'inactive': gettext_lazy("Usuario inativo."),
        }
        
        AuthenticationForm.error_messages = error_messages

        return super().form_invalid(form)



class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'home/dashboard.html'
    form_class = NovoFunciForm
    def get(self, request):
        form = self.form_class()
        user = self.request.user
        autenticado = user.is_authenticated
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        print(f"##############{user}#################")
        return render(request,self.template_name,{'form':form,'autenticado':autenticado,'funcionarios':lista})


    def post(self, request):
        form = self.form_class(request.POST)
        
        # create a form instance and populate it with data from the request:
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.usuario = self.request.user
            # funcionario = Funcionario.objects.all().order_by('-id')[0]
            funcionario.save()
            return HttpResponseRedirect(f"/dashboard/")
        

class ListFuncionarios(LoginRequiredMixin,ListView):
    model = Funcionario

    template_name = 'home/tables-bootstrap-tables.html'
    def get(self, request):
        user = self.request.user
        user = self.request.user
        autenticado = user.is_authenticated
        if autenticado:
            lista = Funcionario.objects.filter(usuario=user)
        else:
            lista = ''
        return render(request, self.template_name,{"page_obj":lista,"autenticado":autenticado})
    
class FuncionarioDetailView(LoginRequiredMixin,DetailView):
    model = Funcionario
    template_name = 'funcionario_detail.html'
    def get_queryset(self):
        user = self.request.user

        funcionario_id = self.kwargs['pk']
        return Funcionario.objects.filter(id=funcionario_id,usuario=user)

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm  # Substitua pelo caminho real do seu formulário
from .models import Funcionario  
from django.http import JsonResponse

class AuthorCreateView(LoginRequiredMixin, FormView):
    template_name = 'funcionario_create.html'
    form_class = ContactForm
    success_url = reverse_lazy('create_funci')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.usuario = self.request.user
        funcionario.save()
        return JsonResponse({'nome': funcionario.nome})  # Retornar o nome do funcionário

    def form_invalid(self, form):
        return JsonResponse({'error': 'Erro ao cadastrar funcionário.'}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        autenticado = user.is_authenticated
        lista = Funcionario.objects.filter(usuario=user).order_by('-id')
        context['autenticado'] = autenticado
        context['funcionarios'] = lista
        return context
