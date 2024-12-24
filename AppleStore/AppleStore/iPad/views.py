from django.http import HttpResponse
from django.template import loader
from .models import iPad

def iPads(request):
  myiPad = iPad.objects.all().values()
  template = loader.get_template('iPadShop.html')
  context = {
    'myiPad': myiPad,
  }
  return HttpResponse(template.render(context, request))

def iPadDetails(request, iPad_id):
  myiPad = iPad.objects.get(pk=iPad_id)
  template = loader.get_template('iPadDetails.html')
  context = {
    'myiPad': myiPad,
  }
  return HttpResponse(template.render(context, request))