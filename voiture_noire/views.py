from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views import generic, View

from archives.models import Author, Fic
from .models import DiscordProfile, Prompt

from .models import DiscordProfile
from .forms import DiscordProfileForm, PromptForm

# Create your views here.
class Index(generic.ListView):
    template_name = 'voiture_noire/index.html'
    context_object_name = 'fics'

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if Author.objects.filter(member=user).exists():
                story_author = Author.objects.get(member=user)
                return Fic.objects.filter(Q(author=story_author) | Q(visible=True)).order_by('-date')
            else:
                return Fic.objects.filter(visible=True)
        else:
            return Fic.objects.filter(visible=True, visible_not_member_only=True).order_by('-date')
            

class MemberList(generic.ListView):
    template_name = 'voiture_noire/memberList.html'
    context_object_name = 'DiscordProfiles'

    def get_queryset(self):
        return DiscordProfile.objects.order_by('member__username')    


class Profile(generic.View):
    form_class = DiscordProfileForm
    template_name = 'voiture_noire/profile.html'
    initial = {}

    def get(self, request, *args, **kwargs):
        user_stories = []
        author_profile = None
        discord_member = DiscordProfile.objects.filter(member=request.user).first()

        if discord_member:
            self.initial = discord_member
            discord_form = self.form_class(instance=self.initial)
            author_profile = Author.objects.filter(member=request.user).first() 
            if author_profile:
                user_stories = Fic.objects.filter(author=author_profile)
        else:
            self.initial = {"likes": "", "dislikes": ""}
            discord_form = self.form_class(initial=self.initial)

        return render(
            request,
            self.template_name,
            {"author_profile": author_profile, "form": discord_form, "stories": user_stories})
    
    def post(self, request, *args, **kwargs):
        new_profile = DiscordProfileForm(request.POST)
        if new_profile.is_valid():
            discord_member = DiscordProfile.objects.get_or_create(member=request.user)[0]
            instance = new_profile.save(commit=False)
            discord_member.likes = instance.likes
            discord_member.dislikes = instance.dislikes
            discord_member.member = request.user
            discord_member.save()
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

        if criteria == "supporters":
            prompt_list = Prompt.objects.annotate(number_of_supporters=Count('supporters')).order_by("number_of_supporters")
        elif criteria == "pairing_type":
            prompt_list = Prompt.objects.order_by(criteria, "body")
        elif criteria == "user_likes":
            prompt_list = Prompt.objects.annotate(
                has_supporter=Count(
                    'supporters', filter=Q(supporters__id=request.user.id)
                )).order_by('-has_supporter', 'body')
            print(prompt_list)
        else:
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
        if author.criminal:
            author.criminal = False
        else:
            author.criminal = True
        author.save()

    return redirect('voiture_noire:profile')

