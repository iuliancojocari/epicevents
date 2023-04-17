from django.urls import path, include
from rest_framework import routers
from .views import ClientViewSet, ContractViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r"clients", ClientViewSet, basename="clients")
router.register(r"contracts", ContractViewSet, basename="contracts")
router.register(r"events", EventViewSet, basename="events")


urlpatterns = [
    path(r"", include(router.urls)),
]
