from django.db import models
from accounts.models import Member


class DiscordMember(Member):
    likes = models.TextField(max_length=1500, blank=True, null=True)
    dislikes = models.TextField(max_length=1500, blank=True, null=True)

class Prompt(models.Model):
    PAIRING_TYPE = [
    ("MM", "M/M"),
    ("FF", "F/F"),
    ("F/M", "Hétéro"),
    ("ETC", "Autre"),
    ("GEN", "Général"),
    ]
    body = models.TextField(max_length=300)
    pairing_type = models.CharField(max_length=3, choices=PAIRING_TYPE)
    supporters = models.ManyToManyField(
        Member, 
        blank=True,
        null=True,
    )
