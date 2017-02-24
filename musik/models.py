from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	isActive = models.BooleanField()
	numAlbums = models.IntegerField()

	def __str__(self):
		return self.name+" : "+self.genre

class Album(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	releaseDate = models.DateTimeField()
	numSongs = models.IntegerField()
	duration = models.IntegerField()
	avgRating = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title, self.genre

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=100)
	releaseDate = models.DateTimeField()
	duration = models.IntegerField()
	avgRating = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.title, self.genre