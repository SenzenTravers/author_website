from django import forms

from .models import DiscordProfile, Prompt, ServerEvent


class DiscordProfileForm(forms.ModelForm):
    class Meta:
        model = DiscordProfile
        fields = ["member", "likes", "dislikes", 'birthday']


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]


class ServerEvent(forms.ModelForm):
    class Meta:
        model = ServerEvent
        fields = ['event_type', 'title', 'event_start', 'event_end']