from django.urls import path
from . import views

app_name = 'push'

urlpatterns = [
    path('', views.posts_list, name='dise'), #this is for lay.html
    path('<slug:slug>', views.rats, name='pray') # this is for posts_list.html
]
