from django.urls import path

from . import views

app_name = 'gadgets'

urlpatterns = [
    path("", views.index, name="index"),
    path("yaoi-generator", views.yaoi_generator, name="yaoi_generator"),
    path("ecritoire", views.word_counter, name="ecritoire")
    # path('', views.Index.as_view(), name='index'),
]