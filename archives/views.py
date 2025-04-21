import os
import tempfile

from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic


from xhtml2pdf import pisa

from .forms import Author, ChapterForm, FicForm
from .models import Chapter, Fic, PairingType
from .utils import check_user_has_right, FicDigester


class Index(generic.ListView):
    template_name = 'archives/index.html'
    context_object_name = 'fics'


    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Fic.objects.filter(visible=True).order_by('-date')
        else:
            return Fic.objects.filter(visible=True, visible_not_member_only=True).order_by('-date')



class PublishView(generic.View):
    template_name = 'archives/voiture_noire_publish.html'
    chapter_form = ChapterForm
    fic_form = FicForm

    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        fic_form = self.fic_form(initial=self.initial)
        chapter_form = self.chapter_form(initial=self.initial)
        return render(
            request,
            self.template_name,
            {
                "chapter_form": chapter_form,
                "fic_form": fic_form,
            }
        )
    
    def post(self, request, *args, **kwargs):
        fic_form = FicForm(request.POST)
        chapter_form = ChapterForm(request.POST)

        # fic_form.errors

        if fic_form.is_valid() & chapter_form.is_valid():
            fic_author = Author.objects.get_or_create(
                member=request.user,
                defaults={"nickname": request.user.username}
            )[0]
            fic_instance = fic_form.save(commit=False)
            fic_instance.clap = 0
            fic_instance.author = fic_author
            fic_instance.save()
            new_fic = Fic.objects.filter(author=fic_author).latest("id")
            pairing_types = fic_form.cleaned_data["pairing_type"]
            pairing_types = PairingType.objects.filter(id__in=pairing_types)
            new_fic.pairing_type.set(pairing_types)
            new_fic.save()
            chapter_form = chapter_form.save(commit=False)
            chapter_form.fic = new_fic
            chapter_form.save()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre fic."
            )
        return redirect('archives:publish')

class StoryReadMode(generic.View):
    template_name = 'archives/story_read_mode.html'

    def get(self, request, fic_id, number, *args, **kwargs):
        request_user = self.request.user
        story_author = Author.objects.get(member=request_user)
        fic = get_object_or_404(Fic, pk=fic_id)

        if (fic.visible == False and fic.author == story_author) or \
            (fic.visible == True and fic.visible_not_member_only == False and request_user.is_authenticated) or \
            (fic.visible == True and fic.visible_not_member_only == True):
            chapter = Chapter.objects.get(fic=fic, number=number)
            return render(
                request,
                self.template_name,
                {
                    "story": fic,
                    "chapter": chapter
                }
            )
        else:
            return redirect('voiture_noire:index')



class FicEditView(generic.View):
    template_name = 'archives/voiture_noire_fic_edit.html'
    chapter_form = ChapterForm
    fic_form = FicForm

    def get(self, request, fic_id, number, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=fic_id)
        chapter = Chapter.objects.get(fic=fic, number=1)
        fic_form = self.fic_form(initial=self.initial)
        chapter_form = self.chapter_form(initial=self.initial)

        return render(
            request,
            self.template_name,
            {
                "fic_form": fic_form,
                "chapter_form": chapter_form
            }
        )
    # def get(self, request, *args, **kwargs):
    #     fic_form = self.fic_form(initial=self.initial)
    #     chapter_form = self.chapter_form(initial=self.initial)
    #     return render(
    #         request,
    #         self.template_name,
    #         {
    #             "chapter_form": chapter_form,
    #             "fic_form": fic_form,
    #         }
    #     )


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