from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views import generic, View

from archives_api.models import APIFic

from .models import DiscordProfile
from .forms import DiscordProfileForm, PromptForm

# Create your views here.
class Index(generic.ListView):
    template_name = 'voiture_noire/index.html'
    context_object_name = 'APIfics'

    def get_queryset(self):
        return APIFic.objects.order_by('-date')

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


class Prompt(View):
    form_class = PromptForm
    initial = {"key": "value"}
    template_name = "voiture_noire/prompts.html"


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect("/")

        return render(request, self.template_name, {"form": form})
