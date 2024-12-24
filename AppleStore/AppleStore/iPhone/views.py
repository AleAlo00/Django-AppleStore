from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import iPhone
from .forms import iPhoneForm

def iPhones(request):
  myiPhone = iPhone.objects.all().values()
  template = loader.get_template('iPhoneShop.html')
  context = {
    'myiPhone': myiPhone,
  }
  return HttpResponse(template.render(context, request))

def iPhoneDetails(request, iPhone_id):
  myiPhone = get_object_or_404(iPhone, id=iPhone_id)

  if request.method == 'POST':
      form = iPhoneForm(request.POST, instance=myiPhone)
      if form.is_valid():
          form.save()
  else:
      form = iPhoneForm(instance=myiPhone)

  return render(request, 'iPhoneDetails.html', {'myiPhone': myiPhone, 'form': form})

def iPhoneShop(request):
    myiPhone = iPhone.objects.all().values()
    template = loader.get_template('Shop.html')
    context = {
        'myiPhone': myiPhone,
    }
    return HttpResponse(template.render(context, request))


def AppleStore(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())