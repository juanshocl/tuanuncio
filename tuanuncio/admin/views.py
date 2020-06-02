from django.shortcuts import render
from publish.models import advertisement
from django.views.generic import ListView

# Create your views here.

class admList(ListView):
     loop_range = range (1,6)
     model = advertisement
     template_name = 'admin/admin_list.html'