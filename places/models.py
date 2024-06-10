from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.CharField(max_length=200)
    description_long = models.TextField()

    def __str__(self):
        return str(self.title)


class PlaceImage(models.Model):
    url = models.URLField()
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='imgs'
    )

    def __str__(self) -> str:
        return str(self.url)


class PlaceCoordinate(models.Model):
    lng = models.FloatField()
    lat = models.FloatField()
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='coords'
    )
