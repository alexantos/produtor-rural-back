from django.urls import include, path
from rest_framework import routers

from api.cultura.views import CulturaView
from api.plantio.views import PlantioView
from api.produtor.views import ProdutorView
from api.propriedade.views import PropriedadeView
from api.safra.views import SafraView
from api.views import grafico_estados, grafico_culturas, grafico_uso_solo, cards_produtor

router = routers.DefaultRouter()
router.register(r'cultura', CulturaView)
router.register(r'produtor', ProdutorView)
router.register(r'propriedade', PropriedadeView)
router.register(r'safra', SafraView)
router.register(r'plantio', PlantioView)

urlpatterns = [
    path('', include(router.urls)),
    path('grafico-estados/', grafico_estados),
    path('grafico-culturas/', grafico_culturas),
    path('grafico-uso-solo/', grafico_uso_solo),

    path('cards-produtor/', cards_produtor),
]
