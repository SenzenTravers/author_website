from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'voiture_noire'

urlpatterns = [
    # path('', views.Index.as_view(), name='index'),
    path('', login_required(views.Profile.as_view()), name='index'),
    path('profile', login_required(views.Profile.as_view()), name='profile'),
    path('everyone', login_required(views.MemberList.as_view()), name='everyone'),
    path('prompts', login_required(views.PromptView.as_view()), name='prompts'),
    path('post_prompt', login_required(views.post_prompt), name='post_prompt'),
    path('unfavourite/<int:prompt_id>', views.unfavourite, name='unfavourite'),
    path('favourite/<int:prompt_id>', views.favourite, name='favourite'),

]