from random import randint
from datetime import date, datetime

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views import generic, View

from archives.models import Author, Story
from .models import ExchangeParticipant, Prompt

from .models import ExchangeParticipant
from .forms import ExchangeParticipantForm, PromptForm


class Index(generic.ListView):
    template_name = 'voiture_noire/index.html'
    context_object_name = 'stories'

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Story.objects.filter(
                Q(author__member_id=user.id) | (~Q(visibility='Private') & Q(story_date__lte=date.today()))
            ).order_by('-story_date')
        else:
            return Story.objects.filter(
                Q(visibility='Everyone') & (Q(story_date__lte=date.today()))
            ).order_by('-story_date')
            

class MemberList(generic.ListView):
    template_name = 'voiture_noire/memberList.html'
    context_object_name = 'ExchangeParticipants'

    def get_queryset(self):
        # TODO: later on, filter on member active status
        return ExchangeParticipant.objects.all().order_by('member__username')


class Profile(View):
    form_class = ExchangeParticipantForm
    template_name = 'voiture_noire/profile.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        user_stories = []
        author_profile = Author.objects.filter(member=request.user).first() 
        exchange_participant = ExchangeParticipant.objects.filter(member=request.user).first()

        if exchange_participant is None and author_profile is None:
            raise PermissionDenied()

        self.initial = exchange_participant
        discord_form = self.form_class(instance=self.initial)
        random_rec = None
        potential_recs = Story.objects.filter(
            ~Q(author=author_profile) & (~Q(visibility='Private') & Q(story_date__lte=date.today()))
        )
        
        if len(potential_recs) > 1:
            random_rec = potential_recs[
                randint(0, len(potential_recs) -1)
            ]
        else:
            random_rec = potential_recs[0]

        if author_profile:
            user_stories = Story.objects.filter(author=author_profile)


        return render(
            request,
            self.template_name,
            {
                "exchange_participant": exchange_participant,
                "author_profile": author_profile,
                "form": discord_form,
                "stories": user_stories,
                "random_rec": random_rec
            }
        )
    
    def post(self, request, *args, **kwargs):
        new_profile = ExchangeParticipantForm(request.POST)
        if new_profile.is_valid():
            exchange_participant = ExchangeParticipant.objects.get_or_create(member=request.user)[0]
            instance = new_profile.save(commit=False)
            exchange_participant.likes = instance.likes
            exchange_participant.dislikes = instance.dislikes
            exchange_participant.member = request.user
            exchange_participant.save()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre profil. Veuillez garder chaque champ en-dessous de 3000 caractères."
            )
        return redirect('voiture_noire:profile')
        

class PromptView(View):
    form_class = PromptForm
    initial = {"key": "value"}
    template_name = "voiture_noire/prompts.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        prompt_list = Prompt.objects.order_by('-id')

        return render(request, self.template_name, {
            "form": form,
            "prompt_list": prompt_list
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        criteria = request.POST['sort_value']
        match criteria:
            case "supporters":
                prompt_list = Prompt.objects.annotate(number_of_supporters=Count('supporters')).order_by("number_of_supporters")
            case "pairing_type":
                prompt_list = Prompt.objects.order_by(criteria, "body")
            case "user_likes":
                prompt_list = Prompt.objects.annotate(
                    has_supporter=Count(
                        'supporters', filter=Q(supporters__id=request.user.id)
                    )).order_by('-has_supporter', 'body')
            case _:
                prompt_list = Prompt.objects.order_by(criteria)
        return render(request, self.template_name, {
            "form": form,
            "prompt_list": prompt_list
            })

def post_prompt(request):
    new_prompt = PromptForm(request.POST)
    if new_prompt.is_valid():
        saved_prompt = new_prompt.save()
        saved_prompt.supporters.add(request.user)
        return redirect('voiture_noire:prompts')
    # Todo: return message for ano

def favourite(request, prompt_id):
    try:
        prompt = Prompt.objects.get(id=prompt_id)
        prompt.supporters.add(request.user)
    except:
        return redirect('500')
    return redirect('voiture_noire:prompts')

def unfavourite(request, prompt_id):
    try:
        prompt = Prompt.objects.get(id=prompt_id)
        prompt.supporters.remove(request.user)
    except:
        return redirect('500')
    return redirect('voiture_noire:prompts')

def brand_as_criminal(request, author_id):
    author = Author.objects.filter(member=request.user).first()

    if author and request.user == author.member :
        author.criminal = not author.criminal # toggle the value ON/OFF
        author.save()

    return redirect('voiture_noire:profile')
