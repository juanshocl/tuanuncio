from django.shortcuts import render
from django.views.generic import ListView
from publish.models import advertisement

# Create your views here.
class publish(ListView):
    model = advertisement
    template_name = 'publish/publish.html'
