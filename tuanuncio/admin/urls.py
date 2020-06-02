from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/list',views.admList.as_view(), name='admList'),
]