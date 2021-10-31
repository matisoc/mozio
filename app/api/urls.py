from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .views import ServiceAreaViewSet, ProviderViewSet

router = DefaultRouter()
router.register('providers', ProviderViewSet)
router.register('service-areas', ServiceAreaViewSet)

schema_view = get_swagger_view(title='Monzio API')

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', schema_view)
]

