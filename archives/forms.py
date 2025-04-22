import datetime

from django import forms

from .models import Author, Chapter, Fic, PairingType

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ChapterForm(forms.ModelForm):
    publish_date = forms.DateField(
        widget = forms.SelectDateWidget(years=range(2005, 2026)),
    )

    class Meta:
        model = Chapter
        fields = '__all__'


class FicForm(forms.ModelForm):
    G = "g"
    T = "t"
    E = "e"

    RATING_TYPE_CHOICES = {
        G: "Tout public",
        T: "Public averti",
        E: "Adulte",
    }

    date = forms.DateField(
        widget = forms.SelectDateWidget(years=range(2005, 2026))
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
        model = Fic
        fields = '__all__'

    def __init__(self, *arg, **kwargs):
        super(FicForm, self).__init__(*arg, **kwargs)
        self.fields["text_length"].initial = "SHORT"
        self.fields["rating"].initial = "t"


class PairingTypeForm(forms.ModelForm):
    class Meta:
        model = PairingType
        fields = '__all__'

# FOR PUBLISHING
