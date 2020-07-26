from django.db import models

class Processo(models.Model):   #Modelo Processo
    pasta   = models.TextField()
    comarca = models.TextField()
    uf      = models.TextField()
