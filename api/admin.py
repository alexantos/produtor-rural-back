from django.contrib import admin

from api.cultura.models import Cultura
from api.plantio.models import Plantio
from api.produtor.models import Produtor
from api.propriedade.models import Propriedade
from api.safra.models import Safra

admin.site.register(Cultura)
admin.site.register(Produtor)
admin.site.register(Propriedade)
admin.site.register(Safra)
admin.site.register(Plantio)
