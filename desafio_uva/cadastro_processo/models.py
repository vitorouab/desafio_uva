from django.db import models

class Planilha(models.Model):   #Modelo Planilha
    nome    = models.TextField()
    cliente = models.TextField()
    arquivo = models.FileField()
