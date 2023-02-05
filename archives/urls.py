from django.urls import path

from . import views

app_name = 'archives'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('stories/<int:fic_id>', views.first_chapter, name='first_chapter'),
    # path('stories/<int:pk>', views.firstChapter.as_view(), name='first_chapter'),
    path('stories/chapter/<int:pk>', views.ChapterView.as_view(), name='chapter'),
]