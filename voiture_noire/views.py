from random import randint
from datetime import date, datetime

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.http import JsonResponse
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
        return DiscordProfile.objects.filter(is_creator=True).order_by('member__username')    


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
            count = Fic.objects.count()
            random_rec = None
            potential_recs = Fic.objects.filter(
                ~Q(author=author_profile) & (
                    (Q(visible=True)| Q(visible_not_member_only=True))
                )
            )
            
            if len(potential_recs) > 1:
                random_rec = potential_recs[randint(0, count-1)]
            else:
                random_rec = potential_recs[0]

            if author_profile:
                user_stories = Fic.objects.filter(author=author_profile)
        else:
            raise PermissionDenied()

        return render(
            request,
            self.template_name,
            {
                "author_profile": author_profile,
                "form": discord_form,
                "stories": user_stories,
                "random_rec": random_rec
            }
        )
    
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


class DiscordProfilesBirthdaysUpdateView(generic.edit.UpdateView):
    form_class = DiscordProfileForm
    template_name = 'voiture_noire/profile.html'
    initial = {}
 
    def update(self, request, *args, **kwargs):
        profile = DiscordProfileForm(request.POST)
        if profile.is_valid():
            discord_member = DiscordProfile.objects.get(member=request.user)
            #to do what if object does not exists ?
            instance = profile.save(commit=False)
            # discord_member.likes = instance.likes
            # discord_member.dislikes = instance.dislikes
            # discord_member.member = request.user
            discord_member.birthday = instance.birthday
            discord_member.save()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Une erreur est survenue durant l'enregistrement de votre profil. Veuillez garder chaque champ en-dessous de 3000 caractères."
            )
        return redirect('voiture_noire:profile')
       


## View functions
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

def discord_profiles_birthdays(request):
    # Get date from request, default to today if not provided
    date_param = request.GET.get('date') or request.POST.get('date')
    
    if date_param:
        try:
            query_date = datetime.strptime(date_param, '%Y-%m-%d').date()
        except ValueError:
            query_date = date.today()
    else:
        query_date = date.today()
    
    profiles = DiscordProfile.objects.filter(birthday__isnull=False).select_related('member')
    data = [
        {
            'member_id': profile.member.id if profile.member else None,
            'member_username': profile.member.username if profile.member else None,
            'birthday': profile.birthday.isoformat() if profile.birthday else None
        }
        for profile in profiles if profile.birthday and profile.birthday == query_date
    ]
    return JsonResponse({'members_birthdays': data, 'query_date': query_date.isoformat()})

