from hashlib import blake2b
from pydoc import describe
from django.db import models

class Event(models.Model):
    text = models.TextField(default='')
    show = models.BooleanField(default=False)

    def __str__(self):
        return "Upozornění na vrcholu stránky (nepřidávat další, jen měnit tenhle)"

class Report(models.Model):
    thumbnail = models.ImageField()
    title = models.CharField(max_length=100, blank=True)
    text = models.TextField(blank=True)
    date = models.DateField()

    def __str__(self):
        title = 'žádný'
        if self.title != '':
            title = self.title
        return 'titulek: ' + title + ' | datum: ' + str(self.date)

class Home_image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return "fotografie na hlavní stránku: " + self.image.name

class Gallery(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

class Gallery_image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "galerie: " + self.gallery.name + " | popisek: " + self.description + " | obrázek: " + self.image.name

class Visitor_counter(models.Model):
    name = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'počet načtení stránky ' + self.name + ": " + str(self.count)