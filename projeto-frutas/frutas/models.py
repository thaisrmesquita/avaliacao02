from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grupo(models.Model):
    name = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    #owner = models.ForeignKey('auth.User', related_name='grupos', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class Fruta(models.Model):
    name = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.CharField(max_length=255, default='')
    #Grupo não poderá mais ser nulo.
    #grupo = models.ForeignKey(Grupo, related_name='frutas', on_delete=models.CASCADE, null=True)
    grupo = models.ForeignKey(Grupo, related_name='frutas', on_delete=models.CASCADE)
    #Relacionamento com o usuário que criou
    #owner = models.ForeignKey('auth.User', related_name='frutas', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

class Propriedade(models.Model):
    name = models.CharField(max_length=255)
    descricao = models.TextField()
    fruta = models.ForeignKey(Fruta, related_name='propriedades', on_delete=models.CASCADE)
    #owner = models.ForeignKey('auth.User', related_name='propriedades', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name



class Curiosidade(models.Model):
    name = models.CharField(max_length=255)
    descricao = models.TextField()
    fruta = models.ForeignKey(Fruta, related_name='curiosidades', on_delete=models.CASCADE)
    #owner = models.ForeignKey('auth.User', related_name='curiosidades', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
