# pedidos/models.py
from django.db import models
from django.contrib.auth import get_user_model
from itens.models import Item  # Certifique-se de importar o modelo Item corretamente

class Pedido(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item, through='PedidoItem')

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
