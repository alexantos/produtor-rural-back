from rest_framework import viewsets, permissions

from api.safra.models import Safra
from api.safra.serializers import SafraSerializer


class SafraView(viewsets.ModelViewSet):
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []
