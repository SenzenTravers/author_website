from rest_framework import serializers

from accounts.models import Member
from archives.models import Chapter, Fic
from models import APIFic

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = [
            'url', 'username', 'email'
        ]

class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        # fields = [
        #     'url', 'username', 'email'
        # ]

class APIFicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIFic