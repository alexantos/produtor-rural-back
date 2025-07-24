from rest_framework import serializers

from api.produtor.serializers import ProdutorSerializer
from api.propriedade.models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'
