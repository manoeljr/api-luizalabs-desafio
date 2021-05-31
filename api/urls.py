from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ClienteViewset, ProdutoViewset


router = SimpleRouter()


router.register('clientes', ClienteViewset)
router.register('produtos', ProdutoViewset)
