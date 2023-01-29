from django.urls import path

from . import views

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('', views.Homepage.as_view(), name='homepage'),
    path('about', views.about, name='about'),
]