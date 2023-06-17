import os
import tempfile

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.

from .models import Fic, Chapter


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

class FicDigester:
    def __init__(self):
        # ID to call to DB and return a Chapter and Fic Object
        print("Nothing")

    def create_file(self, data):
        # Later, need a format_for_html thing
        # Infos to format stuff
        title, path = tempfile.mkstemp(suffix=".html", text=True)

        fic = str.encode(data, "utf-8")
        os.write(title, fic)
        try:
            self.download_file(request)
        except Exception as e:
            print(e)

        os.close(title)
        os.remove(path)

    def download_file(self, request):
        fic = "/tmp/tmps0y34d_0.html"
        resp = HttpResponse('')

        with  open(fic, 'r') as tmp:
            filename = tmp.name.split('/')[-1]
            resp = HttpResponse(tmp, content_type='application/text;charset=UTF-8')
            resp['Content-Disposition'] = "attachment; filename=%s" % filename

        return resp

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
