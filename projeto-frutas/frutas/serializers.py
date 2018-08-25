
from rest_framework import serializers
from .models import *


class FrutaSerializer(serializers.HyperlinkedModelSerializer):
    #Grupo não poderá mais ser nulo.
    #grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field="name", allow_null=True)
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field="name")
    propriedades = serializers.SlugRelatedField(queryset=Propriedade.objects.all(), slug_field="descricao", many=True)
    curiosidades = serializers.SlugRelatedField(queryset=Curiosidade.objects.all(), slug_field="descricao", many=True)
    #usuario que criou a fruta
    #owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Fruta
        #fields = ("url", "id", "owner", "name", "descricao", "imagem", "grupo", "propriedades", "curiosidades")
        fields = ("url", "id", "name", "descricao", "imagem", "grupo", "propriedades", "curiosidades")

class FrutaDetailSerializer(serializers.HyperlinkedModelSerializer):
    #Grupo não poderá mais ser nulo.
    #grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field="name", allow_null=True)
    grupo = serializers.SlugRelatedField(queryset=Grupo.objects.all(), slug_field="name", allow_null=True)
    #owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
         model = Fruta
         #fields = ("url", "owner", "name", "descricao", "imagem", "grupo", "propriedades", "curiosidades")
         fields = ("url", "name", "descricao", "imagem", "grupo", "propriedades", "curiosidades")


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Grupo
        # Não eh necessário mostrar o campo 'owner'
        fields = ("url", "id", "name", "descricao")


class GrupoDetailSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Grupo
        #fields = ("url", "owner", "name", "descricao", "frutas")
        fields = ("url", "name", "descricao", "frutas")

class PropriedadeSerializer(serializers.HyperlinkedModelSerializer):
    fruta = serializers.SlugRelatedField(queryset=Fruta.objects.all(), slug_field="name")
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Propriedade
        # Não eh necessário mostrar o campo 'owner'
        fields = ("url", "id", "name", "descricao", "fruta")

class PropriedadeDetailSerializer(serializers.HyperlinkedModelSerializer):
    fruta = serializers.SlugRelatedField(queryset=Fruta.objects.all(), slug_field="name")
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Propriedade
        #fields = ("url", "owner", "name", "descricao", "fruta")
        fields = ("url", "name", "descricao", "fruta")

class CuriosidadeSerializer(serializers.HyperlinkedModelSerializer):
    fruta = serializers.SlugRelatedField(queryset=Fruta.objects.all(), slug_field="name")
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Curiosidade
        # Não eh necessário mostrar o campo 'owner'
        fields = ("url", "id", "name", "descricao", "fruta")

class CuriosidadeDetailSerializer(serializers.HyperlinkedModelSerializer):
    fruta = serializers.SlugRelatedField(queryset=Fruta.objects.all(), slug_field="name")
    #owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Curiosidade
        #fields = ("url", "owner", "name", "descricao", "fruta")
        fields = ("url", "name", "descricao", "fruta")

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        #User deve mostrar apenas as frutas.
        #Não precisa mostrar proprieades e curiosidades, embora tenha a lista das mesmas que criou.
        #fields = ("url", "id", "username", "frutas")
        fields = ("url", "id", "username")

