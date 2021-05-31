from .models import Cliente, Produto
from .serializers import ClienteSerializer, ProdutoSerializer

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ClienteViewset(viewsets.ModelViewSet):
    """ API desafio LuizaLabs """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=True, methods=['get'])
    def produtos(self, request, pk=None):
        """ Buscando todos produtos de um cliente """
        cliente = self.get_object()
        serializer = ProdutoSerializer(cliente.produtos.all(), many=True)
        return Response(serializer.data)


class ProdutoViewset(viewsets.ModelViewSet):
    """ API desafio LuizaLabs """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer