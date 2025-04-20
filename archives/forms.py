from django import forms

from .models import Author, Chapter, Fic, PairingType

# class MemberCreationForm(UserCreationForm):
#     class Meta:
#         model = Member
#         fields = ('username', 'email', 'password1', 'password2')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'


class FicForm(forms.ModelForm):
    class Meta:
        model = Fic
        fields = '__all__'


class PairingTypeForm(forms.ModelForm):
    class Meta:
        model = PairingType
        fields = '__all__'

# FOR PUBLISHING
