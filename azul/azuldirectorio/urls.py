from django.conf.urls import url
from azuldirectorio.views import *

urlpatterns = [

    url(r'^directorio', Directorio.as_view(), name='azuldirectorio'),
]