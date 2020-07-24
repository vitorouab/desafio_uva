from django.db import models

class Processo(models.Model):
    pasta   = models.TextField()
    comarca = models.TextField()
    uf      = models.TextField()
