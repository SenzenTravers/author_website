import datetime

from django import forms

from .models import Author, Chapter, Comment, Story, PairingType

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'nickname', 'criminal',
            'trackbear_profile', 'other_profile_url'
        ]


class ChapterForm(forms.ModelForm):
    publishing_date = forms.DateField(
        widget = forms.SelectDateWidget(years=range(2005, 2027))
    )

    class Meta:
        model = Chapter
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class StoryForm(forms.ModelForm):
    G = "g"
    T = "t"
    E = "e"

    RATING_TYPE_CHOICES = {
        G: "Tout public",
        T: "Public averti",
        E: "Adulte",
    }

    story_date = forms.DateField(
        widget = forms.SelectDateWidget(years=range(2005, 2027))
    )
    pairing_type = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=PairingType.objects.all()
    )
    rating = forms.ChoiceField(
        widget=forms.Select,
        choices=RATING_TYPE_CHOICES,
    )

    class Meta:
        model = Story
        fields = '__all__'

    def __init__(self, *arg, **kwargs):
        super(StoryForm, self).__init__(*arg, **kwargs)
        self.fields["text_length"].initial = "SHORT"
        self.fields["rating"].initial = "t"


class PairingTypeForm(forms.ModelForm):
    class Meta:
        model = PairingType
        fields = '__all__'

# FOR PUBLISHING
