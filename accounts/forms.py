from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('username', 'email', 'password1', 'password2')

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('username', 'email')
