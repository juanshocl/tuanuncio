from django.urls import path, include
from . import views


urlpatterns = [
    path('publish', views.publish.as_view(), name='publish'),
    #path('',views.index.as_view(), name='index'),
]