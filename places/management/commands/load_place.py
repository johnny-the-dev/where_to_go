import logging
from io import BytesIO

import requests
from django.core.exceptions import ValidationError
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from requests.exceptions import RequestException

from places.models import Place, PlaceCoordinate, PlaceImage

logger = logging.getLogger("commands.load_place")


class Command(BaseCommand):
    help = 'Load places into the database from a given URL'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        url = options['urls'][0]

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except RequestException as error:
            logger.error('Failed to load place: %s', error)
            return

        place_data = response.json()
        coordinates = place_data.pop('coordinates', {})
        imgs = place_data.pop('imgs', [])

        try:
            place = Place(**place_data)
            place.full_clean()
        except ValidationError as validation_error:
            for field, messages in validation_error.message_dict.items():
                for message in messages:
                    logger.error('%s: %s', field, message)
            return
        place.save()

        if coordinates:
            PlaceCoordinate.objects.get_or_create(
                place=place,
                lat=coordinates.get('lat', ''),
                lng=coordinates.get('lng', ''),
            )
        else:
            logger.warning('Place %s has no coordinates', place.title)

        for number, img_url in enumerate(imgs, 1):
            try:
                img_response = requests.get(img_url, timeout=5)
                img_response.raise_for_status()
            except RequestException as img_error:
                logger.warning('Failed to load image: %s', img_error)
                continue

            buffer = BytesIO(img_response.content)
            image_file = ImageFile(buffer, name=img_url.split('/')[-1])
            PlaceImage.objects.create(
                place=place,
                image=image_file,
                number=number
            )

        logger.info('Place %s loaded successfully', place.title)
