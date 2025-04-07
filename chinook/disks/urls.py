from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),  # Liste des albums
    path('disks/<int:album_id>/', views.album_detail, name='album_detail'),  # Détails de l'album
]
