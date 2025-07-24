from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from api.propriedade.filters import PropriedadeFilter
from api.propriedade.models import Propriedade
from api.propriedade.serializers import PropriedadeSerializer


class PropriedadeView(viewsets.ModelViewSet):
    queryset = Propriedade.objects.all()
    serializer_class = PropriedadeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []

    filter_backends = [DjangoFilterBackend]
    filterset_class = PropriedadeFilter
