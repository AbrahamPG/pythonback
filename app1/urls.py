from django.urls import path
from . import views


urlpatterns = [
    path('app1_list/', views.app1_list, name='app1_list')

]