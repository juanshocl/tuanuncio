from django.shortcuts import render, redirect
from publish.models import advertisement, region, comuna
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
import csv
import codecs
import urllib
from pip._vendor import requests


# Create your views here.

class admList(ListView):
     model = advertisement
     template_name = 'admin/admin_list.html'

class adminCreate(CreateView):
     model = advertisement
     fields = ['User', 
               'name',
               'Type_advertisement',
               'description',
               'comuna',
               'whatsapp',
               'show_phones',
               'email',
               'url_website',
               'address',
               'show_adress', 
               'Userfacebook',
               'UserInstagram',
               'UserTwitter',
               'state']

     template_name = 'admin/admin_form.html'
     success_url = reverse_lazy('admList')

class adminUpdate(UpdateView):
     model = advertisement
     fields = ['User', 
               'name',
               'Type_advertisement',
               'description',
               'comuna',
               'whatsapp',
               'show_phones',
               'email',
               'url_website',
               'address',
               'show_adress', 
               'Userfacebook',
               'UserInstagram',
               'UserTwitter',
               'state']
     template_name = 'admin/admin_form.html'
     success_url = reverse_lazy('admList')
     
class adminDelete(DeleteView):
     model = advertisement
     template_name  = 'admin/admin_delete.html'
     success_url  = reverse_lazy('admList')


def adminActivar(request, pk): 
     if advertisement.objects.values('state').filter(id=pk)[0]['state']:
          maintenance = advertisement.objects.filter(id=pk).update(state=False)
     else:
          maintenance = advertisement.objects.filter(id=pk).update(state=True)
     return redirect ('admList')

def comunas(request):
    # Datos de Consumiendo desde un archivo CSV
     url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'
     ftpfile = urllib.request.urlopen(url)
     csvfile = csv.reader(codecs.iterdecode(ftpfile, 'utf-8'))
     bandera = 0
     for column in csvfile:
          if bandera > 0:
               _, created = comuna.objects.get_or_create(
               Reg=region.objects.get(Codregion=column[1]),
               ComunaName=column[2],
               CodComuna=column[3],
               )
          bandera = bandera + 1
     return redirect ('admList')


def regiones(request):
    # Datos de Region, Codigo, Nombre, Poblacion, Etc Desde una API.
     urlAPI = 'https://chile-coronapi.herokuapp.com/api/v3/models/regions'
     response = requests.get(urlAPI)
     if response.status_code == 200:
          response_json = response.json()
          for key in response_json:
               if int(key) < 10:
                    llave = '0'+key
               else:
                    llave = key
               _, created = region.objects.get_or_create(
               Codregion=llave,
               RegionName=response_json[key]['region']
               )
     return redirect ('admList')