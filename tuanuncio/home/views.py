from django.shortcuts import render
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
