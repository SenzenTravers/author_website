from rest_framework import permissions, viewsets

from accounts.models import Member
from archives.models import Chapter
from models import APIFic
from serializers import ChapterSerializer, APIFicSerializer, MemberSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticated]

class FicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = APIFic.objects.all()
    serializer_class = APIFicSerializer
    permission_classes = [permissions.IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-username')
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]
