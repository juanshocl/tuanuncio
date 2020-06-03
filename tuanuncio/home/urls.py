from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index.as_view(), name='index'),
    path('validation/',views.validation, name='validation' ),
    #path('publish/', views.pubList.as_view(), name='pubList'),
]

