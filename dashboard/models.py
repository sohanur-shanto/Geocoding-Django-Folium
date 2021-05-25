from django.db import models
import geocoder

# Create your models here.

class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longtitude = models.FloatField(default=0)


    class Meta:
        verbose_name_plural = 'Data'


    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.country).lat
        self.longtitude = geocoder.osm(self.country).lng
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.country


class Search(models.Model):

    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Search'

    def __str__(self):
        return self.address