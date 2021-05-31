from rest_framework import serializers
from .models import Cliente, Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'preco', 'imagem', 'titulo', 'cliente']


class ClienteSerializer(serializers.ModelSerializer):
    # Buscando todos produtos no cliente(Relationship)
    produtos = ProdutoSerializer(many=True, read_only=True)

    class Meta:
        extra_kargs = {'email': {'write_only': True}}
        model = Cliente
        fields = ['id', 'nome', 'email', 'produtos']
