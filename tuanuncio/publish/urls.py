from django.urls import path, include
from . import views



urlpatterns = [
    path('publish/', views.pubList.as_view(), name='pubList'),
    path('publish/nuevo', views.pubCreate.as_view(), name='pubNuevo'),
    path('publish/update/<pk>', views.pubUpdate.as_view(), name='pubUpdate'),
    path('publish/delete/<pk>', views.pubDelete.as_view(), name='pubDelete'),

    
    #path('publish/', views.publish.as_view(), name='publish'),
    #path('',views.index.as_view(), name='index'),
]