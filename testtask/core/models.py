from django.db import models


class POICategories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name
# Create your models here.
class POI(models.Model):
    id = models.AutoField(primary_key=True)
    internal_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.internal_id

class POIRatings(models.Model):
    id = models.AutoField(primary_key=True)
    poi = models.ForeignKey(POI, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
