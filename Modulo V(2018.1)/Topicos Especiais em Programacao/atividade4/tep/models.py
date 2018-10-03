from django.db import models


# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    idade = models.CharField(max_length=200, blank=False)
    altura = models.CharField(max_length=200, blank=False)
    nacionalidade = models.CharField(max_length=200, blank=False)
    image = models.ImageField(blank=False, null=False)
    useruser = models.ForeignKey('users.User', blank=False, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    body = models.TextField(blank=False, null=False)
    post = models.ForeignKey('Post', blank=False, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
