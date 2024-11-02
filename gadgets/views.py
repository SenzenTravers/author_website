from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
# from .models import Fic, Chapter

from .ressources import YaoiGenerator

def index(request):
    return render(
        request,
        'gadgets/grenier.html'
        )

def yaoi_generator(request):
    prompt = YaoiGenerator.return_random_prompt()
    response = JsonResponse({"result": prompt})
    return response
# class Index(generic.ListView):
#     template_name = 'archives/index.html'
#     context_object_name = 'fics'

#     def get_queryset(self):
#         return Fic.objects.order_by('-date')

# def first_chapter(request, fic_id):
#     fic = get_object_or_404(Fic, pk=fic_id)
#     chapters = Chapter.objects.filter(fic=fic_id).order_by('id')
#     current_chapter = chapters[0]

#     return render(
#         request,
#         'archives/story.html',
#         {'fic':fic,
#         'chapters': chapters,
#         'current_chapter': current_chapter
#         })

# class ChapterView(generic.DetailView):
#     model = Chapter
#     template_name = 'archives/story.html'