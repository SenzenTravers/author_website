from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View

from archives_api.models import APIFic

from .models import DiscordMember
from .forms import DiscordMemberForm, PromptForm

# Create your views here.
class Index(generic.ListView):
    template_name = 'voiture_noire/index.html'
    context_object_name = 'APIfics'

    def get_queryset(self):
        return APIFic.objects.order_by('-date')

class Profile(generic.View):
    form_class = DiscordMemberForm
    template_name = 'voiture_noire/profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

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
