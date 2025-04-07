from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Album
from django.db.models import Q

def album_list(request):
    search_query = request.GET.get('search', '')  # Récupérer la recherche de l'utilisateur
    albums = Album.objects.all()

    if search_query:
        albums = albums.filter(title__icontains=search_query)

    return render(request, 'disks/album_list.html', {'albums': albums, 'search_query': search_query})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    tracks = album.tracks.all()  # Obtenir tous les titres associés à l'album
    return render(request, 'disks/album_detail.html', {'album': album, 'tracks': tracks})