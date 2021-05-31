import uuid
from django.db import models


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    titulo = models.CharField(max_length=255, unique=True)
    imagem = models.URLField(null=True, unique=True)
    preco = models.FloatField(max_length=255)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='produtos')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.titulo
