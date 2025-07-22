from rest_framework import viewsets, permissions

from api.cultura.models import Cultura
from api.cultura.serializers import CulturaSerializer


class CulturaView(viewsets.ModelViewSet):
    queryset = Cultura.objects.all()
    serializer_class = CulturaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []