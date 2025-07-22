from rest_framework import viewsets, permissions

from api.produtor.models import Produtor
from api.produtor.serializers import ProdutorSerializer


class ProdutorView(viewsets.ModelViewSet):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = []
