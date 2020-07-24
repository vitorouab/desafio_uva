from django.db import models

class Planilha(models.Model):
    nome    = models.TextField()
    cliente = models.TextField()
    arquivo = models.FileField()
