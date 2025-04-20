from django.db import models

from accounts.models import Member



# UTILS CLASSES
class ChapterManager(models.Manager):
    def return_next_number(fic):
        return Chapter.objects.filter(fic=fic).count() + 1


class PairingType(models.Model):
    pairing_type = models.CharField(max_length=5, unique=True)


# TRUE CLASSES
class Author(models.Model):
    member = models.ForeignKey(Member,
        on_delete=models.CASCADE,
        null=True)
    nickname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nickname


class Fic(models.Model):
    G = 'g'
    T = 't'
    E = 'e'

    GEN = 'gen'
    FF = 'F/F'
    MM = 'M/M'
    HET = 'F/M'
    OTHER = 'autre'

    # TODO: manytomany relationship    
    # PAIRING_CHOICES = [
    #     (GEN, 'Pas de couple'),
    #     (FF, 'F/F'),
    #     (MM, 'M/M'),
    #     (HET, 'Hétéro'),
    #     (OTHER, 'Autre')

    RATING_CHOICES = [
        (G, 'G'),
        (T, 'T'),
        (E, 'E')
    ]

    SHORT = 'nouvelle'
    NOVELLA = "novella"
    NOVEL = 'roman'
    SERIES = 'series'
    
    LENGTH_CHOICES = [
        (SHORT, 'Nouvelle'),
        (NOVELLA, 'Novella'),
        (NOVEL, 'Roman'),
        (SERIES, 'Série')
    ]

    author = models.ForeignKey(Author,
        on_delete=models.CASCADE,
        null=True)
    visible_member_only = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    clap = models.IntegerField(default=0)
    date = models.DateField(null=True)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=600)
    author_note = models.TextField(max_length=2000, blank=True)
    pairing_archetype = models.CharField(max_length=200, blank=True)
    one_sentence_summary = models.CharField(max_length=200, blank=True)
    pairing_type = models.ManyToManyField(
        PairingType, 
        blank=True,
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
    fic = models.ForeignKey(Fic, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    author_note = models.TextField(max_length=1500, null=True, blank=True)
    content = models.TextField(max_length=1000000)

    objects = ChapterManager()
    
    def save(self, *args, **kwargs):
        if self.number == None:
            self.number = self.objects.return_next_number(self.fic)
            super(Chapter, self).save(*args, **kwargs)
        else:
            super(Chapter, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fic}, chapter {self.number}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fic', 'number'], name="unique_chapter_number_for_fic")
        ]

# TO ADD: concept de série
