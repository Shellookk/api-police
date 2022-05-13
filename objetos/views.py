from rest_framework import viewsets
from objetos.models import Arma, Municao
from objetos.serializer import ArmaSerializer, MunicaoSerializer

class ArmasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as armas"""
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer

class MunicaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as munições"""
    queryset = Municao.objects.all()
    serializer_class = MunicaoSerializer
