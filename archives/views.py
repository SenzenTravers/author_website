from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Fic


class Index(generic.ListView):
    template_name = 'archives/index.html'
    context_object_name = 'fics'

    def get_queryset(self):
        return Fic.objects.order_by('-date')