from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic, View

from archives_api.models import APIFic
from .models import DiscordProfile, Prompt

from .models import DiscordProfile
from .forms import DiscordProfileForm, PromptForm

# Create your views here.
class Index(generic.ListView):
    template_name = 'voiture_noire/index.html'
    context_object_name = 'APIfics'

    def get_queryset(self):
        return APIFic.objects.order_by('-date')


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
        try:
            discord_member = DiscordProfile.objects.get(
                member=request.user
            )
            self.initial = discord_member
            form = self.form_class(instance=self.initial)
        except:
            self.initial = {"likes": "", "dislikes": ""}
            form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        new_profile = DiscordProfileForm(request.POST)
        if new_profile.is_valid():
            discord_member = DiscordProfile.objects.get_or_create(member=request.user)[0]
            instance = new_profile.save(commit=False)
            discord_member.likes = instance.likes
            discord_member.dislikes = instance.dislikes
            discord_member.member = request.user
            discord_member.save()
        return redirect('voiture_noire:profile')


class PromptView(View):
    form_class = PromptForm
    initial = {"key": "value"}
    template_name = "voiture_noire/prompts.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        prompt_list = Prompt.objects.order_by('body')

        return render(request, self.template_name, {
            "form": form,
            "prompt_list": prompt_list
            }
        )

    def post(self, request, *args, **kwargs):
        new_prompt = PromptForm(request.POST)
        if new_prompt.is_valid():
            saved_prompt = new_prompt.save()
            saved_prompt.supporters.add(request.user)
        return redirect('voiture_noire:prompts')

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
