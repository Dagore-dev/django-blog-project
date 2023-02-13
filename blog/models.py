from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    author = models.ForeignKey('auth.User', verbose_name='Autor', on_delete=models.CASCADE)
    body = models.TextField('Cuerpo')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
