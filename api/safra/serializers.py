from rest_framework import serializers

from api.safra.models import Safra


class SafraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safra
        fields = '__all__'
