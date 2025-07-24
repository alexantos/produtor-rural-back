import django_filters

from api.produtor.models import Produtor


class ProdutorFilter(django_filters.FilterSet):
    class Meta:
        model = Produtor
        fields = {
            'nome': ['iexact'],
        }
