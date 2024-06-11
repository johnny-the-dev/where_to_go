from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.CharField(max_length=200)
    description_long = models.TextField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return str(self.title)


class PlaceImage(models.Model):
    number = models.IntegerField(verbose_name="Номер картинки", null=True, blank=True)
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images", verbose_name='Локация')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self) -> str:
        return f'{self.number or ""} "{self.place.title}"'


class PlaceCoordinate(models.Model):
    lng = models.CharField(max_length=10)
    lat = models.CharField(max_length=10)
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE, primary_key=True, related_name="coords"
    )

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"

    def __str__(self):
        return f'"{self.place.title}"'
