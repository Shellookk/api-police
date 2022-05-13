from django.contrib import admin
from objetos.models import Arma, Municao



#classe Armas
class Armas(admin.ModelAdmin):
    list_display = ('id', 'calibre_arma', 'marca_arma', 'modelo_arma', 'quantidade_tiros','valor_estimado_arma','imagem')
    list_display_links = ('id','marca_arma','modelo_arma','calibre_arma')
    search_fields = ('marca_arma','modelo_arma',) 
    list_per_page = 20

admin.site.register(Arma,Armas)

#classe Munições
class Municoes(admin.ModelAdmin):
    list_display = ('id','calibre_municao', 'marca_municao', 'modelo_municao','valor_estimado_municao')
    list_display_links = ('id','marca_municao','modelo_municao','calibre_municao')
    search_fields = ('marca_municao','modelo_municao',) 

admin.site.register(Municao,Municoes)