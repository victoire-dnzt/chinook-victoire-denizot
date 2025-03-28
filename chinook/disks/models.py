from django.db import models

# Create your models here.
from django.db import models

class Artist (models.Models):
    name = models.CharField(max_length=255)
    
def __str__(self):
        return self.name

class Album (models.Models):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Un album appartient à un artiste

    def __str__(self):
        return self.name

class Track (models.Models):
    name = models.CharField(max_length=255)
    composer = models.CharField(max_length=255)  # compositeur de la chanson
    milliseconds = models.IntegerField()  # durée en millisecondes
    bytes = models.IntegerField()  # taille du fichier en octets
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)  # prix de la piste
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # une piste appartient à un album

    def __str__(self):
        return self.name