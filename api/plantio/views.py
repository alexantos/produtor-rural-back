from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from api.plantio.filters import PlantioFilter
from api.plantio.models import Plantio
from api.plantio.serializers import PlantioSerializer


class PlantioView(viewsets.ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []

    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantioFilter
