from django.db import models


# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    idade = models.CharField(max_length=200, blank=False)
    altura = models.CharField(max_length=200, blank=False)
    nacionalidade = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='photos', max_length=254)

    def __str__(self):
        return self.nome
