from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',views.index.as_view(), name='index'),
    path('validation/',login_required(views.validation), name='validation' ),
    #path('publish/', views.pubList.as_view(), name='pubList'),
]

