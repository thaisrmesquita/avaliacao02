from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *
from rest_framework import generics
from .permissions import *
import json


# Create your views here.


class FrutaList(generics.ListCreateAPIView):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer
    name = 'fruta-list'
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly,
    )
    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    '''

class FrutaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruta.objects.all()
    serializer_class = FrutaDetailSerializer
    name = 'fruta-detail'
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly
    )

class GrupoList(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    name = 'grupo-list'
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly
    )
    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    '''

class GrupoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoDetailSerializer
    name = 'grupo-detail'
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly
    )

class PropriedadeList (generics.ListCreateAPIView):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    name = "propriedade-list"
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly,
    )
    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    '''


class PropriedadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeDetailSerializer
    name = "propriedade-detail"
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly,
    )

class CuriosidadeList (generics.ListCreateAPIView):
    queryset = Curiosidade.objects.all()
    serializer_class = CuriosidadeSerializer
    name = "curiosidade-list"
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly,
    )
    '''
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    '''

class CuriosidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curiosidade.objects.all()
    serializer_class = CuriosidadeDetailSerializer
    name = "curiosidade-detail"
    permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly,
    )

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"
    permission_classes = (
            permissions.IsAuthenticated,
    )

class UserDetail (generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    )

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
                         'frutas': reverse(FrutaList.name, request=request),
                         'grupos': reverse(GrupoList.name, request=request),
                         'propriedades': reverse(PropriedadeList.name, request=request),
                         'curiosidades': reverse(CuriosidadeList.name, request=request),
                         'users': reverse(UserList.name, request=request)
                         })

