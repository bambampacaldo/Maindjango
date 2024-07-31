from django.urls import path
from . import views

app_name = 'uzers'

urlpatterns = [
    path('registers/', views.reg, name='registers'),
    path('login/', views.login_view, name='login'),
]
