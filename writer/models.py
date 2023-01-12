from accounts.models import Member
from django.db import models


class Author(models.Model):
    member = models.ForeignKey(Member,
        on_delete=models.CASCADE,
        )
    nickname = models.CharField(max_length=100, unique=True)


class Fic(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True
    )
    clap = models.IntegerField(default=0)
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=1000)
    author_note = models.TextField(max_length=1000)


class Chapter(models.Model):
    fic = models.ForeignKey(Fic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    content = models.TextField(max_length=50000)


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
