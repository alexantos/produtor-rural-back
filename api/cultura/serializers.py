from rest_framework import serializers

from api.cultura.models import Cultura


class CulturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultura
        fields = '__all__'
