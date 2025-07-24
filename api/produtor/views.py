from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from api.produtor.filters import ProdutorFilter
from api.produtor.models import Produtor
from api.produtor.serializers import ProdutorSerializer


class ProdutorView(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdutorFilter
