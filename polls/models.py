from django.db import models

class Pessoas(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=10)