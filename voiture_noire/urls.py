from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'voiture_noire'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile', login_required(views.Profile.as_view()), name='profile'),
    path('everyone', login_required(views.MemberList.as_view()), name='everyone'),
    path('prompts', login_required(views.Prompt.as_view()), name='prompts'),
]