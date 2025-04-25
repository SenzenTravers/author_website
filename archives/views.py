import datetime
import tempfile

from django.contrib import messages
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic


from xhtml2pdf import pisa

from .forms import Author, ChapterForm, FicForm
from .models import Chapter, Fic, PairingType
from .utils import FicDigester


class Index(generic.ListView):
    template_name = 'archives/index.html'
    context_object_name = 'fics'


    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Fic.objects.filter(visible=True).order_by('-date')
        else:
            return Fic.objects.filter(visible=True, visible_not_member_only=True).order_by('-date')


class StoryReadMode(generic.View):
    template_name = 'archives/story_read_mode.html'

    def get(self, request, fic_id, number, *args, **kwargs):
        request_user = self.request.user

        fic = get_object_or_404(Fic, pk=fic_id)

        if (fic.visible == False and fic.author.member == request.user) or \
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

############## POSTING
class PublishView(generic.View):
    template_name = 'archives/voiture_noire_publish.html'
    chapter_form = ChapterForm
    fic_form = FicForm

    def get(self, request, *args, **kwargs):
        fic_form = self.fic_form(
            initial={"date": datetime.date.today()}
        )
        chapter_form = self.chapter_form(
            initial={"publish_date": datetime.date.today()}

        )
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
            chapter_form.number = 1
            chapter_form.save()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre fic."
            )
        return redirect('voiture_noire:index')


class ChapterPostView(generic.View):
    template_name = 'archives/voiture_noire_chapter_post.html'
    chapter_form = ChapterForm

    def get(self, request, fic_id, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=fic_id)

        if request.user != fic.author.member:
            redirect('voiture_noire:index')
    
        return render(
            request,
            self.template_name,
            {
                "chapter_form": self.chapter_form,
                "story": fic
            }
        )

    def post(self, request, fic_id, *args, **kwargs):
        root_fic = Fic.objects.get(id=fic_id)
        chapter_nb = root_fic.number_of_chapter + 1

        if request.user != root_fic.author.member:
            redirect('voiture_noire:index')

        chapter_form = ChapterForm(request.POST)

        # # fic_form.errors

        if chapter_form.is_valid():
            chapter_form = chapter_form.save(commit=False)
            chapter_form.fic = root_fic
            chapter_form.number = chapter_nb
            chapter_form.save()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre fic."
            )
        return redirect('voiture_noire:index')


##### EDITING
class ChapterEditView(generic.View):
    template_name = 'archives/voiture_noire_chapter_edit.html'
    chapter_form = ChapterForm

    def get(self, request, fic_id, number, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=fic_id)
        chapter = get_object_or_404(Chapter, fic=fic, number=number)

        if request.user != fic.author.member:
            redirect('voiture_noire:index')
    
        chapter_form = self.chapter_form(instance=chapter)

        return render(
            request,
            self.template_name,
            {
                "chapter_form": chapter_form,
                "fic": fic
            }
        )

    def post(self, request, fic_id, number, *args, **kwargs):
        root_fic = Fic.objects.get(id=fic_id)

        if request.user != root_fic.author.member:
            redirect('voiture_noire:index')

        chapter_form = ChapterForm(request.POST)

        # # fic_form.errors
        if chapter_form.is_valid():
            chapter_initial_instance = Chapter.objects.get(fic=root_fic, number=number)
            chapter_form = chapter_form.save(commit=False)
            chapter_initial_instance.chapter_title = chapter_form.chapter_title
            chapter_initial_instance.author_note = chapter_form.author_note
            chapter_initial_instance.content = chapter_form.content
            chapter_initial_instance.publish_date = chapter_form.publish_date
            chapter_initial_instance.save()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre fic."
            )
        return redirect('voiture_noire:index')
        

class FicEditView(generic.View):
    template_name = 'archives/voiture_noire_story_edit.html'
    fic_form = FicForm

    def get(self, request, fic_id, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=fic_id)
        chapters = Chapter.objects.filter(fic=fic)

        if request.user != fic.author.member:
            redirect('voiture_noire:index')
    

        fic_form = self.fic_form(
            instance=fic,
        )

        return render(
            request,
            self.template_name,
            {
                "fic_form": fic_form,
                "chapters": chapters,
                "fic_id": fic.id
            }
        )

    def post(self, request, fic_id, *args, **kwargs):
        fic_initial_instance = Fic.objects.get(id=fic_id)
        # NOTE : passer aussi les chapitres existants en arg
        if request.user != fic_initial_instance.author.member:
            redirect('voiture_noire:index')

        fic_form = FicForm(request.POST)

        if fic_form.is_valid():
            fic_instance = fic_form.save(commit=False)
            fic_initial_instance.fic_title = fic_instance.fic_title
            fic_initial_instance.visible_not_member_only = fic_instance.visible_not_member_only
            fic_initial_instance.visible = fic_instance.visible
            fic_initial_instance.date = fic_instance.date
            fic_initial_instance.summary = fic_instance.summary
            fic_initial_instance.fic_author_note = fic_instance.fic_author_note
            fic_initial_instance.pairing_archetype = fic_instance.pairing_archetype
            fic_initial_instance.one_sentence_summary = fic_instance.one_sentence_summary
            fic_initial_instance.rating = fic_instance.rating
            fic_initial_instance.text_length = fic_instance.text_length
            fic_initial_instance.complete = fic_instance.complete

            pairing_types = fic_form.cleaned_data["pairing_type"]
            pairing_types = PairingType.objects.filter(id__in=pairing_types)
            fic_initial_instance.pairing_type.set(pairing_types)
            fic_initial_instance.save()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'édition de votre récit. Désolée !"
            )
        return redirect('voiture_noire:index')


##### DELETING
def delete_story(request, story_id):
    story = get_object_or_404(Fic, pk=story_id)

    if request.user == story.author.member:
        story.delete()
        return redirect('voiture_noire:profile')
    else:
        raise HttpResponseNotAllowed("Vous n'êtes pas l'auteur de cette histoire !")
    
def delete_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    if request.user == chapter.fic.author.member:
        chapter.delete()
        return redirect('voiture_noire:profile')
    else:
        raise HttpResponseNotAllowed("Vous n'êtes pas l'auteur de cette histoire !")

########## OLD
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

################ UTILS
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