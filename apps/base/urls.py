from django.urls import path
from apps.base.views import index, chef_detail

urlpatterns = [
    path ('', index, name= 'index'),
    path('chef_detail/<int:id>/', chef_detail, name='chef_detail')
          
]
