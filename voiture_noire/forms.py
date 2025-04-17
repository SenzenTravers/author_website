from django import forms

from .models import DiscordProfile, Prompt


class DiscordProfileForm(forms.ModelForm):
    class Meta:
        model = DiscordProfile
        fields = ["member", "likes", "dislikes"]

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]