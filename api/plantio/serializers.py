from rest_framework import serializers

from api.plantio.models import Plantio


class PlantioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantio
        fields = '__all__'
