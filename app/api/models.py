from django.contrib.gis.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField, CurrencyField
from phonenumber_field.modelfields import PhoneNumberField
 
class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField()
    language =  models.CharField(
        max_length = 7, choices = settings.LANGUAGES,
        blank = False, null = False)
    currency = CurrencyField(default='USD')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    area = models.PolygonField()
    price_amount = MoneyField(max_digits=25, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']