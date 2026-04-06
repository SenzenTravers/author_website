import datetime
import tempfile

from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from archives.forms import Author, ChapterForm, StoryForm
from archives.models import Chapter, Story, PairingType
from archives.utils import StoryDigester


class ChapterPostView(generic.View):
    template_name = 'archives/voiture_noire_chapter_post.html'
    chapter_form = ChapterForm

    def get(self, request, story_id, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=story_id)

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

    def post(self, request, story_id, *args, **kwargs):
        root_fic = Fic.objects.get(id=story_id)
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


class ChapterEditView(generic.View):
    template_name = 'archives/voiture_noire_chapter_edit.html'
    chapter_form = ChapterForm

    def get(self, request, story_id, number, *args, **kwargs):
        fic = get_object_or_404(Fic, pk=story_id)
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

    def post(self, request, story_id, number, *args, **kwargs):
        root_fic = Fic.objects.get(id=story_id)

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
            chapter_initial_instance.publishing_date = chapter_form.publishing_date
            chapter_initial_instance.save()

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre fic."
            )
        return redirect('voiture_noire:index')

def chapter_delete(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    if request.user == chapter.fic.author.member:
        chapter.delete()
        return redirect('voiture_noire:profile')
    else:
        raise HttpResponseNotAllowed("Vous n'êtes pas l'auteur de cette histoire !")
