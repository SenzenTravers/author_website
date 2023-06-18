import os
import tempfile

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

from .models import Fic, Chapter
from .utils import FicDigester

class Index(generic.ListView):
    template_name = 'archives/index.html'
    context_object_name = 'fics'

    def get_queryset(self):
        return Fic.objects.order_by('-date')

def first_chapter(request, fic_id):
    fic = get_object_or_404(Fic, pk=fic_id)
    chapters = Chapter.objects.filter(fic=fic_id).order_by('id')
    current_chapter = chapters[0]

    return render(
        request,
        'archives/story.html',
        {'fic':fic,
        'chapters': chapters,
        'current_chapter': current_chapter
        })

# class firstChapter(generic.DetailView):
#     model = Chapter
#     template_name = 'archives/story.html'

class ChapterView(generic.DetailView):
    model = Chapter
    template_name = 'archives/story.html'

def download_html(request, fic_id):
    digester = FicDigester(fic_id)
    title = digester.return_title()
    response = HttpResponse(
        digester.html_fic(),
        content_type='text/html',
        headers={'Content-Disposition': f'attachment; filename="{title}.html"'},
    )

    return response

def clap(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    fic = chapter.fic
    fic.clap=fic.clap+1
    fic.save()
    messages.success(request, "Merci pour votre support !")

    return redirect(
        "archives:first_chapter", fic_id=fic.id
        )
# def download_epub(request, fic_id):
#     digester = FicDigester(fic_id)
#     title = digester.return_title()

#     epub = digester.epub_fic()
#     response = HttpResponse(
#         # digester.html_fic(),
#         content_type='text/html',
#         headers={'Content-Disposition': f'attachment; filename="{title}.html"'},
#     )

#     return response