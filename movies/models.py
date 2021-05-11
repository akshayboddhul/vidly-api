from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.ForeignKey("Genre", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    numberInStock = models.IntegerField()
    dailyRentalRate = models.FloatField()

    def __str__(self):
        return self.title
