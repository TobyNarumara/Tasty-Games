from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

import uuid

class Genre(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Article(models.Model):
	name = models.CharField(max_length = 50)
	img = models.ImageField(upload_to = 'uploads/')

	release_date = models.IntegerField()
	genre = models.ManyToManyField(Genre)
	developer = models.CharField(max_length = 50)
	interface_language = models.ManyToManyField(Language, 'Интерфейс')
	voice_language = models.ManyToManyField(Language, 'Озвучка')

	description = RichTextField()

	gameplay = models.CharField(max_length = 250)

	scr = models.ImageField(upload_to = 'uploads/')
	scr2 = models.ImageField(upload_to = 'uploads/')
	scr3 = models.ImageField(upload_to = 'uploads/')
	scr4 = models.ImageField(upload_to = 'uploads/')

	weight = models.CharField(max_length = 50)

	RePack_by = models.CharField(max_length = 50)

	torrent = models.FileField()

	last_update = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name