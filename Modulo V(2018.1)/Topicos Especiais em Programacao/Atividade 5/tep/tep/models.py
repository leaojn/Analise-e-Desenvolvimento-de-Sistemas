from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(blank=False, null=False)
    perfil = models.ForeignKey('users.Perfil', blank=False, on_delete=models.CASCADE, related_name="posts")
    owner = models.ForeignKey(
        'auth.User',
        related_name='posts',
        on_delete=models.CASCADE)
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
