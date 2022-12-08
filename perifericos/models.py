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


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
  
    def todas_categorias():
        return Categoria.objects.all()
  
    def __str__(self):
        return self.nome


class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='images/')
  
    def produtos_por_id(ids):
        return Produtos.objects.filter(id__in=ids)
  
    def todos_produtos():
        return Produtos.objects.all()
  
    def todos_produtos_por_categoriaid(categoria_id):
        if categoria_id:
            return Produtos.objects.filter(categoria=categoria_id)
        else:
            return Produtos.todos_produtos()