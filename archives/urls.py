from django.urls import path

from . import views

app_name = 'archives'

urlpatterns = [
    path('', views.index, name='index'),
]