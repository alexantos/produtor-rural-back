from django.urls import include, path
from rest_framework import routers

from api.cultura.views import CulturaView
from api.produtor.views import ProdutorView
from api.propriedade.views import PropriedadeView
from api.safra.views import SafraView

router = routers.DefaultRouter()
router.register(r'cultura', CulturaView)
router.register(r'produtor', ProdutorView)
router.register(r'propriedade', PropriedadeView)
router.register(r'safra', SafraView)

urlpatterns = [
    path('', include(router.urls)),
]
