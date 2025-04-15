from django.db import models

from archives.models import Fic
# Create your models here.

class APIFic(Fic):
    visibleByAuthenticatedOnly = models.BooleanField(default=False)