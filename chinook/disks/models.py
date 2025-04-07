from django.db import models

# Create your models here.
from django.db import models

class Artist (models.Model):
    name = models.CharField(max_length=255)
    
def __str__(self):
        return self.name

class Album (models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Track (models.Model):
    name = models.CharField(max_length=255)
    composer = models.CharField(max_length=255, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(decimal_places=1,max_digits=3)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return self.name