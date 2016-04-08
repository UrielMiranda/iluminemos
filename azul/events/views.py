from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from .models import *
from eventbrite import Eventbrite


eventbrite = Eventbrite('SRBFZK5OYQYP3CZDHN22')
print(eventbrite)
user = eventbrite.get_user()

print(user)


# Create your views here.
class Eventos(TemplateView):
    model =  EventosModel
    template_name = 'eventos/list.html'