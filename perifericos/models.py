from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=256)
    telefone = models.CharField(max_length=14)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
  
    def registrar(self):
        self.save()
  
    def pegar_cliente_por_email(email):
        try:
            return Cliente.objects.get(email=email)
        except:
            return False
  
    def email_cadastrado(self):
        if Cliente.objects.filter(email=self.email):
            return True
  
        return False