from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/list',views.admList.as_view(), name='admList'),
    path('admin/nuevo', views.adminCreate.as_view(), name='adminCreate'),
    path('admin/update/<pk>', views.adminUpdate.as_view(), name='adminUpdate'),
    path('admin/delete/<pk>', views.adminDelete.as_view(), name='adminDelete'),
    path('admin/activate/<pk>', views.adminActivar, name='adminActivar'),
    path('admin/cargarcomunas',views.comunas, name='comunas'),
    path('admin/cargarregiones',views.regiones, name='regiones'),
    
    

    #path('/done/<int:pk>', views.done, name="done")

]