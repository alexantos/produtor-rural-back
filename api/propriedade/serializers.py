from rest_framework import serializers

from api.produtor.serializers import ProdutorSerializer
from api.propriedade.models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'

    # def to_representation(self, instance):
    #     self.fields['produtor'] = ProdutorSerializer(read_only=True)
    #     return super(PropriedadeSerializer, self).to_representation(instance)
