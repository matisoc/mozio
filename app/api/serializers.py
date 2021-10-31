from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import ServiceArea, Provider

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ("__all__")


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer(read_only=True)
    provider_id = PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        required=True, write_only=True, source='provider')

    class Meta:
        model = ServiceArea
        geo_field = "area"
        fields = ('id', 'name', 'provider', 'provider_id', 'price_amount')
        auto_bbox = True
