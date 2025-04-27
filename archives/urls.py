from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from django.urls import path

from . import views

app_name = 'archives'

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url="https://senestre-coquecigrues.fr/voiture_noire/"),
        name="index",
    ),
    # LUCILE : à ranger plus tard
    # path('', views.Index.as_view(), name='index'),
    # path("<int:fic_id>/html", views.download_html, name="download_html"),
    # path("<int:fic_id>/pdf", views.download_pdf, name="download_pdf"),
    # path("<int:fic_id>/epub", views.download_epub, name="download_epub"),
    # path("<int:fic_id>/clap", views.clap, name="clap"),
    path('stories/publish', login_required(views.PublishView.as_view()), name="story_publish"),
    path('stories/delete/<int:story_id>', login_required(views.delete_story), name="delete_story"),
    path('stories/delete/<int:chapter_id>', login_required(views.delete_chapter), name="delete_chapter"),
    path('stories/edit/<int:fic_id>', login_required(views.FicEditView.as_view()), name="story_edit_mode"),
    path('stories/post/<int:fic_id>', login_required(views.ChapterPostView.as_view()), name="chapter_post_mode"),
    path('stories/edit/<int:fic_id>/chapter/<int:number>', login_required(views.ChapterEditView.as_view()), name="chapter_edit_mode"),
    path('library/<int:fic_id>/<int:number>', views.StoryReadMode.as_view(), name="story_read_mode"),
    path("stories/<int:fic_id>/<int:number>", views.show_chapter, name='show_chapter'),
]