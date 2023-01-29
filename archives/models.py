from accounts.models import Member
from django.db import models


class Author(models.Model):
    member = models.ForeignKey(Member,
        on_delete=models.CASCADE,
        null=True)
    nickname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nickname

class Fic(models.Model):
    GEN = 'gen'
    FF = 'F/F'
    MM = 'M/M'
    HET = 'F/M'
    POLY = 'poly'
    OTHER = 'autre'
    PAIRING_CHOICES = [
        (GEN, 'Pas de couple'),
        (FF, 'Yuri'),
        (MM, 'Yaoi'),
        (HET, 'Hétéro'),
        (POLY, 'Polyamour'),
        (OTHER, 'Autre')
    ]
    G = 'g'
    PG = 'pg'
    PG13 = 'pg-13'
    R = 'r'
    NC17 = 'nc-17'
    RATING_CHOICES = [
        (G, 'G'),
        (PG, 'PG'),
        (PG13, 'PG-13'),
        (R, 'R'),
        (NC17, 'NC-17')
    ]

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True
    )
    clap = models.IntegerField(default=0)
    date = models.DateField(null=True)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=1000)
    author_note = models.TextField(max_length=2000)
    pairing = models.CharField(max_length=200, null=True)
    pairing_type = models.CharField(
        max_length=10,
        choices=PAIRING_CHOICES,
        default=MM
        )
    rating = models.CharField(
        max_length=6,
        choices=RATING_CHOICES,
        default=G
    )
    complete = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.author} : {self.title}"


class Chapter(models.Model):
    fic = models.ForeignKey(Fic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    author_note = models.TextField(max_length=2000, null=True, blank=True)
    content = models.TextField(max_length=50000)

    def __str__(self):
        return f"{self.fic}, chapter number"


class Comment(models.Model):
    author = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        null=True
        )
    chapter = models.ForeignKey(
        Fic,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        max_length=3000
        )

# TO ADD: concept de série
# chapter_number (= automatiquement d'après le compte de chapitre précédent, mais peut être réglé à la main)