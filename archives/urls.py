from django.urls import path

from . import views

app_name = 'archives'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("stories/<int:fic_id>/<int:number>", views.show_chapter, name='show_chapter'),
    path("stories/chapter/<int:pk>", views.ChapterView.as_view(), name='chapter'),
    path("<int:fic_id>/html", views.download_html, name="download_html"),
    path("<int:fic_id>/pdf", views.download_pdf, name="download_pdf"),
    path("<int:fic_id>/epub", views.download_epub, name="download_epub"),
    path("<int:fic_id>/clap", views.clap, name="clap"),
]