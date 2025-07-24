from django_filters import FilterSet

from api.propriedade.models import Propriedade


class PropriedadeFilter(FilterSet):
    class Meta:
        model = Propriedade
        fields = {
            'produtor__id': ['exact'],
            # 'paciente__nome': ['exact', 'iexact', 'contains', 'icontains'],
            # 'data_hora': ['gte', 'lte'],
        }

