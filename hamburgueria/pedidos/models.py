# pedidos/models.py

from django.db import models

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('preparando', 'Preparando'),
        ('finalizado', 'Finalizado'),
    ]
    
    id_pedido = models.AutoField(primary_key=True)
    cliente_nome = models.CharField(max_length=255)
    cliente_endereco = models.CharField(max_length=255)
    produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Pedido #{self.id_pedido} - {self.produto}"

class Preparacao(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    data_iniciada = models.DateTimeField(null=True, blank=True)
    data_finalizada = models.DateTimeField(null=True, blank=True)
    
    def _str_(self):
        return f"Preparação do Pedido #{self.pedido.id_pedido}"

class Finalizado(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    data_entrega = models.DateTimeField(null=True, blank=True)
    
    def _str_(self):
        return f"Pedido #{self.pedido.id_pedido} Finalizado"