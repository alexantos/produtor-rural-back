from rest_framework import viewsets, permissions

from api.plantio.models import Plantio
from api.plantio.serializers import PlantioSerializer


class PlantioView(viewsets.ModelViewSet):
    queryset = Plantio.objects.all()
    serializer_class = PlantioSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []
