from datetime import datetime
import json

from django.conf import settings
from django.shortcuts import render
from django.views import generic

from .models import Post


class Homepage(generic.ListView):
    template_name = 'writer/homepage.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return Post.objects.filter(date__lte=datetime.now()).order_by('-date')

def homepage(request):
    return render(request, 'writer/homepage.html')

def about(request):
    author_profile = ""
    author_json_path = settings.JSON_DIRS / "author_profile.json"

    if not author_json_path.exists():
        author_profile = {
            "about_author_name": "My Name",
            "about_author_blurb": "My Name, a Splendid Wordsmith",
            "about_author_bio": "<p>My Name has had a life.</p><p>My Name also wrote books.</p>"
        }
    else:
        with open(author_json_path, "r", encoding="utf-8") as profile_file:
            author_profile = json.load(profile_file)

    return render(
        request, 'writer/about.html',
        {
            "about_author_name": author_profile["author_name"],
            "about_author_blurb": author_profile["author_blurb"],
            "about_author_bio": author_profile["author_bio"],
            "about_author_bibliography": author_profile["bibliography"]
        }
    )