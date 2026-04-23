from django.db import models
from accounts.models import Member


class ExchangeParticipant(models.Model):
    # TODO: change Meta and related name back to normal
    class Meta:
        db_table = "voiture_noire_discordprofile"

    likes = models.TextField(max_length=3000, blank=True, null=True)
    dislikes = models.TextField(max_length=3000, blank=True, null=True)
    member = models.OneToOneField(
        Member, 
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="exchange_participant"
    )


class Prompt(models.Model):
    PAIRING_TYPE = [
        ("MM", "M/M"),
        ("FF", "F/F"),
        ("F/M", "Hétéro"),
        ("ANY", "N'importe"),
        ("ETC", "Autre"),
        ("GEN", "Général"),
    ]
    body = models.TextField(max_length=300)
    pairing_type = models.CharField(max_length=3, choices=PAIRING_TYPE)
    supporters = models.ManyToManyField(
        Member, 
        blank=True
    )