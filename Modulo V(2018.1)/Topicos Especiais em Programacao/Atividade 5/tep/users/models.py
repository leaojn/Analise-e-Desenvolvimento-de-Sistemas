from django.db import models
from tep.models import Post
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.

class Perfil(models.Model):
    name = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=200,blank=False )
    zipcode = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=200, blank=False)
    suite = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    phone = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def comments(self):
        posts = self.posts.all()
        qtd = 0
        for p in posts:
            qtd += p.comments.all().count()
        return qtd

    def save(self, *args, **kwargs):
        Token.objects.create(user=self.user)

        super(Perfil, self).save(*args, **kwargs)
