from django.db.models import Sum
from rest_framework.decorators import api_view, permission_classes

from api.cultura.models import Cultura
from api.plantio.models import Plantio
from api.propriedade.models import Propriedade
from rest_framework.response import Response


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def grafico_estados(request):
    nomes_estados_distintos = Propriedade.objects.filter().values('estado').distinct()
    grafico_estados = []
    for nome_estado in nomes_estados_distintos:
        grafico_estados.append({
            'descricao': nome_estado['estado'],
            'quantidade': Propriedade.objects.filter(estado=nome_estado['estado']).count(),
        })
    return Response(grafico_estados)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def grafico_culturas(request):
    nomes_culturas_distintos = Cultura.objects.filter().values('descricao').distinct()
    grafico_culturas = []
    for nome_cultura in nomes_culturas_distintos:
        grafico_culturas.append({
            'descricao': nome_cultura['descricao'],
            'quantidade': Plantio.objects.filter(cultura=Cultura.objects.get(descricao=nome_cultura['descricao'])).count(),
        })
    return Response(grafico_culturas)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def grafico_uso_solo(request):
    total_agricultavel = Propriedade.objects.all().aggregate(Sum('area_agricultavel')).get('area_agricultavel__sum', 0)
    total_vegetacao = Propriedade.objects.all().aggregate(Sum('area_vegetacao')).get('area_vegetacao__sum', 0)
    contexto = {
        'total_agricultavel': total_agricultavel,
        'total_vegetacao': total_vegetacao,
    }
    return Response(contexto)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def cards_produtor(request):
    contexto = {}
    id = request.query_params.get('id', None)
    if id is not None:
        propriedades = Propriedade.objects.filter(produtor=id)
        contexto['quantidade_propriedades'] = propriedades.count()
        contexto['total_hectar'] = propriedades.aggregate(Sum('area_total_fazenda')).get('area_total_fazenda__sum', 0)
        contexto['quantidade_culturas'] = Plantio.objects.filter(propriedade__in=propriedades).values('cultura__descricao').distinct().count()
        contexto['quantidade_safras'] = Plantio.objects.filter(propriedade__in=propriedades).values('safra__ano').distinct().count()
    return Response(contexto)