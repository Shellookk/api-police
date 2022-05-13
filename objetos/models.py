from django.db import models



#função para salvar a imagem
def upload_image_arma(instance,filename):
    return f"{instance.modelo_arma}-{filename}"



#classe arma
class Arma(models.Model):
    CALIBRE = (
        ("38", "calibre .38"),
        ("380","calibre .380"),
        ("40", "calibre .40"),
        ("45", "calibre .45"),
        ("N", "não especificado"),
    )
    calibre_arma = models.CharField(max_length=3,choices=CALIBRE,blank=False, null=False,default='N')
    marca_arma = models.CharField(max_length=64)
    modelo_arma = models.CharField(max_length=64)
    quantidade_tiros = models.IntegerField()
    valor_estimado_arma = models.FloatField()
    imagem = models.ImageField(upload_to=upload_image_arma, blank=True, null=True)

    def __str__(self):
        return self.modelo_arma








#classe munição
class Municao(models.Model):
    CALIBRE = (
        ("38", "calibre .38"),
        ("380","calibre .380"),
        ("40", "calibre .40"),
        ("45", "calibre .45"),
        ("N", "não especificado"),
    )
    calibre_municao = models.CharField(max_length=3,choices=CALIBRE,blank=False, null=False,default='N')
    marca_municao  = models.CharField(max_length=64)
    modelo_municao = models.CharField(max_length=64)
    valor_estimado_municao = models.FloatField()

    def __str__(self):
        return self.modelo_municao
