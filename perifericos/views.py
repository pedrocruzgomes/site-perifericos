from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Cliente
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'main/index.html'


class TecladosView(TemplateView):
    template_name = 'main/teclados.html'


class MousesView(TemplateView):
    template_name = 'main/mouses.html'


class HeadsetsView(TemplateView):
    template_name = 'main/headsets.html'


class MousepadsView(TemplateView):
    template_name = 'main/mousepads.html'


class MonitoresView(TemplateView):
    template_name = 'main/monitores.html'


class Login(View):
    return_url = None
  
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'main/login.html')
  
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cliente = Cliente.pegar_cliente_por_email(email)
        error_message = None
        if cliente:
            flag = check_password(senha, cliente.senha)
            if flag:
                request.session['cliente'] = cliente.id
  
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                error_message = 'Suas credenciais estão incorretas!'
        else:
            error_message = 'Suas credenciais estão incorretas!'
  
        print(email, senha)
        return render(request, 'main/login.html', {'error': error_message})
  
  
def logout(request):
    request.session.clear()
    return redirect('login')
  
  
class Signup (View):
    def get(self, request):
        return render(request, 'main/signup.html')
  
    def post(self, request):
        postData = request.POST
        nome = postData.get('nome')
        sobrenome = postData.get('sobrenome')
        telefone = postData.get('telefone')
        email = postData.get('email')
        senha = postData.get('senha')

        value = {
            'nome': nome,
            'sobrenome': sobrenome,
            'telefone': telefone,
            'email': email
        }
        error_message = None
  
        cliente = Cliente(nome=nome,
                            sobrenome=sobrenome,
                            telefone=telefone,
                            email=email,
                            senha=senha)
        error_message = self.validarCliente(cliente)
  
        if not error_message:
            print(nome, sobrenome, telefone, email, senha)
            cliente.senha = make_password(cliente.senha)
            cliente.registrar()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'main/signup.html', data)
  
    def validarCliente(self, cliente):
        error_message = None
        if not cliente.nome:
            error_message = 'Por favor preencha seu nome'
        elif not cliente.sobrenome:
            error_message = 'Por favor preencha seu sobrenome'
        elif not cliente.telefone:
            error_message = 'Por favor preencha seu telefone'
        elif len(cliente.telefone) < 11:
            error_message = 'Número de telefone precisa de pelo menos 11 dígitos'
        elif len(cliente.senha) < 8:
            error_message = 'Sua senha precisa de pelo menos 8 caracteres'
        elif cliente.email_cadastrado():
            error_message = 'Este email já está cadastrado'
  
        return error_message