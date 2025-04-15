import os
import tempfile

from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic


from xhtml2pdf import pisa

from .models import Fic, Chapter
from .utils import FicDigester


class Index(generic.ListView):
    template_name = 'archives/index.html'
    context_object_name = 'fics'

    def get_queryset(self):
        return Fic.objects.order_by('-date')
    
def show_chapter(request, fic_id, number):
    fic = get_object_or_404(Fic, pk=fic_id)
    chapters = Chapter.objects.filter(fic=fic_id).order_by('number')

    current_chapter = chapters[int(number-1)]

    return render(
        request,
        'archives/story.html',
        {'fic':fic,
        'chapters': chapters,
        'current_chapter': current_chapter,
        'number': number
        })

# TODO: REMOVE THESE TWO THINGS
def next_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return Chapter.filter(fic=chapter.fic).filter(number=chapter.number + 1)

def previous_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    return Chapter.filter(fic=chapter.fic).filter(number=chapter.number - 1)

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

def download_pdf(request, fic_id):
    digester = FicDigester(fic_id)
    title = digester.return_title()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

    transformer = pisa.CreatePDF(
        digester.pdf_fic(),
        dest=response,
    )

    if transformer.err:
        return render(
        request,
        'error_500.html'
        )

    return response

def download_epub(request, fic_id):
    digester = FicDigester(fic_id)
    title = digester.return_title()

    response = HttpResponse(
        digester.epub_fic(),
        content_type='application/epub',
        headers={'Content-Disposition': f'attachment; filename="{title}.epub"'},
    )

    return response

def clap(request, fic_id):    
    try:
        fic = Fic.objects.get(id=fic_id)
        fic.clap=fic.clap+1
        fic.save()
        return JsonResponse({"code": 200})
    except:
        return JsonResponse({"code": 500})
    # return redirect(
    #     "archives:first_chapter", fic_id=fic.id
    #     )