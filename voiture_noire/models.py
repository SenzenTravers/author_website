from django.db import models
from accounts.models import Member


class ExchangeParticipant(models.Model):
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
    would_create = models.ManyToManyField(
        Member, 
        blank=True,
        # related_name="would_create"
    )
    # would_receive = models.ManyToManyField(
    #     Member, 
    #     blank=True,
    #     related_name="would_receive"
    # )