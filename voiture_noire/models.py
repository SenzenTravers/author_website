from django.db import models
from accounts.models import Member


class DiscordProfile(models.Model):
    likes = models.TextField(max_length=1500, blank=True, null=True)
    dislikes = models.TextField(max_length=1500, blank=True, null=True)
    member = models.OneToOneField(
        Member, 
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

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
    )
