from datetime import datetime

from django.shortcuts import render
from django.views import generic

from .models import Post


class Homepage(generic.ListView):
    template_name = 'writer/homepage.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.filter(date__lte=datetime.now()).order_by('-date')

def homepage(request):
    return render(request, 'writer/homepage.html')

def about(request):
    return render(request, 'writer/about.html')