from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^galeria/', Artist.as_view(), name='galery'),
]