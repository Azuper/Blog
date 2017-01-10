from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.


class Postt(models.Model):
    titulo = models.CharField(max_length=30)
    cuerpo = models.TextField()
    usuario = models.ForeignKey(User)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Postt'
        verbose_name_plural = 'Postts'

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    comentario = models.CharField(max_length=100)
    usuario = models.ForeignKey(User)
    post = models.ForeignKey(Postt)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.comentario
