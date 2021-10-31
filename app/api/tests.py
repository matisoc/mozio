from collections import OrderedDict
from random import randint

from django.conf import settings
from django.contrib.gis.geos import Polygon
from django.test import TestCase
from django.utils.crypto import get_random_string
from rest_framework_gis.fields import GeoJsonDict

from .models import Provider, ServiceArea
from .serializers import ServiceAreaSerializer

P1 = Polygon([
    [2.109375, 15.29296875],
    [16.083984375, 16.34765625],
    [25.576171875, 0.87890625],
    [-3.69140625, -8.4375],
    [-13.623046875, 12.041015625],
    [-12.568359375, 15.1171875],
    [-11.25, 16.435546875],
    [-8.876953125, 16.611328125],
    [2.109375, 15.29296875]
])

P2 = Polygon([
    [4.5703125, 13.623046875],
    [2.900390625, 9.66796875],
    [5.888671875, 4.658203125],
    [14.58984375, 4.658203125],
    [15.380859375, 14.94140625],
    [6.416015625, 15.64453125],
    [4.5703125, 13.623046875]
])


class SetupTestData:
    def setup_provider(self):
        name = get_random_string()
        email = get_random_string() + "@test.com"
        lng = randint(0, len(settings.LANGUAGES) - 1)
        language = settings.LANGUAGES[lng][0]
        currency = Provider._meta.get_field('currency').default
        return Provider.objects.create(
            name=name, language=language, email=email,
            currency=currency)

    def setup_service_area(self):
        area = Polygon(
                ((0, 0), (0, 10), (10, 10), (0, 10), (0, 0)),
                ((4, 4), (4, 6), (6, 6), (6, 4), (4, 4)))
        provider = self.setup_provider()
        name = get_random_string()
        price_amount = randint(1, 1000)
        return ServiceArea.objects.create(
            area=area, provider=provider,
            name=name, price_amount=price_amount)


class TestModels(SetupTestData, TestCase):
    def test_provider_and_areas(self):
        provider = self.setup_provider()
        area = Polygon(
            ((0, 0), (0, 10), (10, 10), (0, 10), (0, 0)),
            ((4, 4), (4, 6), (6, 6), (6, 4), (4, 4)))
        area1 = self.setup_service_area(area, provider=provider)
        area2 = self.setup_service_area(area, provider=provider)

        self.assertEqual(area1.provider, provider)
        self.assertEqual(area2.provider, provider)
        self.assertEqual(area2.area, area1.area)


class TestSerializers(SetupTestData, TestCase):
    def test_service_area(self):
        name = get_random_string()
        email = name + '@test.com'
        language = 'en'
        currency = 'USD'
        provider = self.setup_provider(
            name=name, email=email, language=language, currency=currency)
        area = self.setup_service_area(
            name=name, provider=provider, price_amount=48)
        serializer = ServiceAreaSerializer(area)
        to_compare =  {
            'geometry': GeoJsonDict([
                ('type', 'Polygon'),
                ('coordinates', [
                    [[0.0, 0.0], [0.0, 10.0], [10.0, 10.0],
                     [0.0, 10.0], [0.0, 0.0]],
                    [[4.0, 4.0], [4.0, 6.0], [6.0, 6.0],
                     [6.0, 4.0], [4.0, 4.0]]])]),
            'bbox': (0.0, 0.0, 10.0, 10.0),
            'type': 'Feature',
            'id': area.id,
            'properties': OrderedDict([
                ('name', name),
                ('provider', OrderedDict([
                    ('id', provider.id),
                    ('name', name),
                    ('email', email),
                    ('phone', ''),
                    ('language', language),
                    ('currency', currency)])),
                ('price_amount', '48.00')])}

        self.assertEqual(serializer.data, to_compare)
