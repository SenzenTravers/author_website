from django import forms

from accounts.models import Member

from .models import ExchangeParticipant, Prompt


class ExchangeParticipantForm(forms.ModelForm):
    class Meta:
        model = ExchangeParticipant
        fields = ["member", "likes", "dislikes"]


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]


class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ["body", "pairing_type"]


class PromptFilterForm(forms.ModelForm):
    will_create_for = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Member.objects.filter(
            exchange_participant__isnull=False
        )
    )
    will_receive_for = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Member.objects.filter(
            exchange_participant__isnull=False
        )
    )
    pairing_type = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Prompt
        fields = [
            "body",
            "pairing_type",
            "will_create_for",
            "will_receive_for"
        ]
