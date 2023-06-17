import os
import tempfile

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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

texte = """
 <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
Ceci est un texte <i>temporaire</i> et <b>audàçiéux</b>.
</body>
</html> 
"""
