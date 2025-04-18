from accounts.models import Member
from django.db import models


class ChapterManager(models.Manager):
    def return_next_number(fic):
        return Chapter.objects.filter(fic=fic).count() + 1

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
    T = 't'
    E = 'e'
    RATING_CHOICES = [
        (G, 'G'),
        (T, 'T'),
        (E, 'E')
    ]

    SHORT = 'nouvelle'
    NOVEL = 'roman'
    LENGTH_CHOICES = [
        (SHORT, 'Nouvelle'),
        (NOVEL, 'Roman'),
    ]

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True
    )
    
    visibleByAdmin = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    clap = models.IntegerField(default=0)
    date = models.DateField(null=True)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=1000)
    author_note = models.TextField(max_length=2000, null=True, blank=True)
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
    text_length = models.CharField(
        max_length=20,
        choices=LENGTH_CHOICES,
        default=SHORT
    )
    complete = models.BooleanField(default=True)


    @property
    def has_multiple_chapters(self):
        if Chapter.objects.filter(fic=self).count() > 1:
            return True
        return False

    def __str__(self):
        return f"{self.author} : {self.title}"


class Chapter(models.Model):
    fic = models.ForeignKey(Fic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    author_note = models.TextField(max_length=2000, null=True, blank=True)
    content = models.TextField(max_length=1000000)

    objects = ChapterManager()
    def __str__(self):
        return f"{self.fic}, chapter {self.number}"
    
    def save(self, *args, **kwargs):
        if self.number == None:
            self.number = self.objects.return_next_number(self.fic)
            super(Chapter, self).save(*args, **kwargs)
        else:
            super(Chapter, self).save(*args, **kwargs)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fic', 'number'], name="unique_chapter_number_for_fic")
        ]


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