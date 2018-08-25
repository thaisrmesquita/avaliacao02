from django.urls import path, include
from django.contrib import admin
from frutas import views

urlpatterns = [
    path('grupos/', views.GrupoList.as_view(), name=views.GrupoList.name),
    path('frutas/', views.FrutaList.as_view(), name=views.FrutaList.name),
    path('propriedades/', views.PropriedadeList.as_view(), name=views.PropriedadeList.name),
    path('curiosidades/', views.CuriosidadeList.as_view(), name=views.CuriosidadeList.name),
    path('propriedades/<int:pk>/', views.PropriedadeDetail.as_view(), name=views.PropriedadeDetail.name),
    path('frutas/<int:pk>/', views.FrutaDetail.as_view(), name=views.FrutaDetail.name),
    path('grupos/<int:pk>/', views.GrupoDetail.as_view(), name=views.GrupoDetail.name),
    path('curiosidades/<int:pk>/', views.CuriosidadeDetail.as_view(), name=views.CuriosidadeDetail.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('api-auth/', include('rest_framework.urls')),
]
