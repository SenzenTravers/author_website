from django.db import models
from accounts.models import Member


class DiscordProfile(models.Model):
    likes = models.TextField(max_length=3000, blank=True, null=True)
    dislikes = models.TextField(max_length=3000, blank=True, null=True)
    is_creator = models.BooleanField(default=True)
    member = models.OneToOneField(
        Member, 
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="discord_profile"
    )
    birthday = models.DateField(null=True, blank=True)


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


class ServerEvent(models.Model):
    event_start = models.DateField()
    event_end = models.DateField()
    EVENT_TYPE = [
        ("conv", "Salon"),
        ("travel", "Voyage")
    ]
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE)
    title = models.CharField(max_length=50)
    actor = models.ForeignKey(DiscordProfile, on_delete=models.CASCADE, related_name="events")