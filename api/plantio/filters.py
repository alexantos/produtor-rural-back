from django_filters import FilterSet

from api.plantio.models import Plantio


class PlantioFilter(FilterSet):
    class Meta:
        model = Plantio
        fields = {
            'propriedade__id': ['exact'],
            # 'paciente__nome': ['exact', 'iexact', 'contains', 'icontains'],
            # 'data_hora': ['gte', 'lte'],
        }
