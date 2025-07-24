from rest_framework import serializers

from api.plantio.models import Plantio


class PlantioSerializer(serializers.ModelSerializer):
    cultura_descricao = serializers.SerializerMethodField()
    safra_descricao = serializers.SerializerMethodField()
    class Meta:
        model = Plantio
        fields = '__all__'

    def get_cultura_descricao(self, obj):
        return obj.cultura.descricao

    def get_safra_descricao(self, obj):
        return obj.safra.ano