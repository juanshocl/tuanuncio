from django.urls import path, include
from . import views



urlpatterns = [
    path('publish/', login_required(views.pubList.as_view()), name='pubList'),
    path('publish/nuevo', login_required(views.pubCreate.as_view()), name='pubNuevo'),
    path('publish/update/<pk>', login_required(views.pubUpdate.as_view()), name='pubUpdate'),
    path('publish/delete/<pk>', login_required(views.pubDelete.as_view()), name='pubDelete'),

    
    #path('publish/', views.publish.as_view(), name='publish'),
    #path('',views.index.as_view(), name='index'),
]