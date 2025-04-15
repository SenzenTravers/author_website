from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'voiture_noire'

urlpatterns = [
    # Login page (set in core ? Redirect here)
    # path("", views.index, name="index"),
    # path("yaoi-generator", views.yaoi_generator, name="yaoi_generator"),
    # path("ecritoire", views.ecritoire, name="ecritoire")
    path('', views.Index.as_view(), name='index'),
    path('profile', login_required(views.Profile.as_view()), name='profile'),
    path('prompts', login_required(views.Prompt.as_view()), name='prompts'),
]