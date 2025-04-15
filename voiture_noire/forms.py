from django import forms

from .models import DiscordMember, Prompt


class DiscordMemberForm(forms.ModelForm):
    class Meta:
        model = DiscordMember
        fields = ["likes", "dislikes"]

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]