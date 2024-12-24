from django.db import models
from slugify import slugify
from tinymce import models as tinymace_models


class Place(models.Model):
    title = models.CharField(max_length=200, db_index=True, unique=True)
    title_full = models.CharField(max_length=200, blank=True)
    place_id = models.SlugField(unique=True, db_index=True, blank=True)
    description_short = models.CharField(max_length=500)
    description_long = tinymace_models.HTMLField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def save(self, *args, **kwargs):
        if not self.title_full:
            self.title_full = self.title

        if not self.place_id:
            self.place_id = slugify(self.title)
            while Place.objects.filter(place_id=self.place_id).exists():
                self.place_id += "1"
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)


class PlaceImage(models.Model):
    number = models.PositiveIntegerField(verbose_name="Позиция", default=0, db_index=True)
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images", verbose_name='Локация')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ("number",)

    def __str__(self) -> str:
        return f'{self.number or ""} "{self.place.title}"'

    def get_absolute_url(self):
        return self.image.storage.url(self.image.name)


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
