from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('admin/list',login_required(views.admList.as_view()), name='admList'),
    path('admin/nuevo', login_required(views.adminCreate.as_view()), name='adminCreate'),
    path('admin/update/<pk>',login_required( views.adminUpdate.as_view()), name='adminUpdate'),
    path('admin/delete/<pk>', login_required(views.adminDelete.as_view()), name='adminDelete'),
    path('admin/activate/<pk>',login_required( views.adminActivar), name='adminActivar'),
    path('admin/cargarcomunas',login_required(views.comunas), name='comunas'),
    path('admin/cargarregiones',login_required(views.regiones), name='regiones'),
    
    

    #path('/done/<int:pk>', views.done, name="done")

]