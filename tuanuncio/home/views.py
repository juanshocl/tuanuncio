from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from publish.models import advertisement

# Create your views here.

# class index(ListView):
#     model = advertisement
#     template_name = 'home/index.html'


# def index(request):
#     context ={}
#     return render(request,'home/index.html', context)

class index(ListView):
    model = advertisement
    template_name = 'home/index.html'

def validation(request):
    if request.user.is_authenticated:
      if request.user.is_staff:
        return redirect('admList')#redirect('admin/list')
      else:
        return redirect('pubList')
    return redirect('auth_login')
