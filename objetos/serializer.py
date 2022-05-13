from rest_framework import serializers
from objetos.models import Arma, Municao

class ArmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arma
        fields = ['id', 'calibre_arma', 'marca_arma', 'modelo_arma', 'quantidade_tiros', 'valor_estimado_arma','imagem']

class MunicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Municao
        fields = ['id','calibre_municao', 'marca_municao', 'modelo_municao','valor_estimado_municao']

