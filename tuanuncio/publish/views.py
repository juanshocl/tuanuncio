from django.shortcuts import render
from publish.models import advertisement
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
# Create your views here.

class pubList(ListView):
     model = advertisement
     template_name = 'publish/publish.html'

     def get_context_data(self, **kwargs):
     context = super(pubList,self).get_context_data(**kwargs)
     adv = advertisement.objects.filter(User = self.user)
     escuelas = School.objects.all().order_by('Name')
     data = []
     for escuela in escuelas:
          promedio = Ratings.objects.filter(Schools=escuela.Id).aggregate(Avg('Score'))['Score__avg']
          dic = {
          'Id': escuela.Id,
          'Name' : escuela.Name,
          'Score': promedio,
          'ImageMD':escuela.ImageMD, 
          'ImageProfile':escuela.ImageProfile,
          'Address':escuela.Address,
          'State_Province':escuela.State_Province,
          'Phone':escuela.Phone, 
          'Type':escuela.Type,
          'Review':escuela.Review,
     }
          data.append(dic)

     context['data'] = data
     return context

# class advCreate(CreateView):
#     model = advertisement
#     form_class = SchoolForm
#     template_name = 'publish/publish_form.html'
#     success_url = reverse_lazy('school_listar')

class pubCreate(CreateView):
     model = advertisement
     #form_class = SchoolForm
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
               'UserTwitter']
     # labels = {
     #           'User': 'Usuario',
     #           'name': 'Nombre',
     #           'Type_advertisement': 'Categoria',
     #           'description': 'Descripcion',
     #           'comuna': 'Comuna' ,
     #           'whatsapp': 'WhatsApp',
     #           'show_phones': '¿Quieres Mostrar tu Telefono?',
     #           'email': 'Email' ,
     #           'url_website': 'Sitio Web',
     #           'address': 'Direccion',
     #           'show_adress' : '¿Mostrar?' , 
     #           'Userfacebook': 'Usuario Facebook',
     #           'UserInstagram': 'Usuario Instagram',
     #           'UserTwitter': 'Usuario Twitter'
     #           }
     # widgets = {
     #        #'User': forms.TextInput(attrs={'class':'form-control'}),
     #        #'Score': forms.Select(attrs={'class':'form-control'}),
     #        'Score': forms.Select(attrs={'class': 'form-control'}),
     #        'Schools': forms.Select(attrs={'class':'form-control'}),
     #    }
     template_name = 'publish/publish_form.html'
     success_url = reverse_lazy('pubList')