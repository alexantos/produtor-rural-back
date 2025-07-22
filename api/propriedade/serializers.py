from rest_framework import serializers

from api.propriedade.models import Propriedade


class PropriedadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propriedade
        fields = '__all__'
