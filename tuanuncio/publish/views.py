from django.shortcuts import render, redirect
from publish.models import advertisement
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
# Create your views here.

class pubList(ListView):
     model = advertisement
     template_name = 'publish/publish.html'

     def get_queryset(self):
          queryset = super(pubList, self).get_queryset()
          queryset = queryset.filter(User=self.request.user)

          return queryset

# def List(request):
#      #queryset = super(pubList, self).get_queryset()
#      #queryset = advertisement.objects.filter(User=request.user)[0]
#      #queryset = advertisement.objects.filter(User=request.user)#advertisement.objects.filter(User=request.user)[0]
#      # data = []
#      # for i in queryset:
#      #      dic = {
#      #           'id': i.id,
#      #           'User': i.User,
#      #           'name': i.name,
#      #           'Type_advertisement': i.Type_advertisement,
#      #           'description': i.description,
#      #           'Userfacebook': i.Userfacebook,
#      #           'UserInstagram': i.UserInstagram,
#      #           'UserTwitter': i.UserTwitter,
#      #           'comuna': i.comuna,
#      #           'whatsapp': i.whatsapp,
#      #           'show_phones': i.show_phones,
#      #           'email': i.email,
#      #           'url_website': i.url_website,
#      #           'address': i.address,
#      #           'show_adress': i.show_adress,
#      #           'incorporation_date': i.incorporation_date,
#      #           'state': i.state,
#      #           }
#      #      data.append(dic)
#      #      con['data'] = data
#      if request.user.is_superuser:
#           return(redirect('admList'))
#      else:
#           return(redirect('pubList'))

# class advCreate(CreateView):
#     model = advertisement
#     form_class = SchoolForm
#     template_name = 'publish/publish_form.html'
#     success_url = reverse_lazy('school_listar')

class pubCreate(CreateView):
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
               'UserTwitter']

     template_name = 'publish/publish_form.html'
     success_url = reverse_lazy('pubList')

class pubUpdate(UpdateView):
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
               'UserTwitter']
     template_name = 'publish/publish_form.html'
     success_url = reverse_lazy('pubList')
     
class pubDelete(DeleteView):
     model = advertisement
     template_name  = 'publish/publish_delete.html'
     success_url  = reverse_lazy('pubList')
