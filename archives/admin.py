from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import Author, Chapter, Fic


class ChapterAdmin(admin.ModelAdmin):
    fields = ['fic', 'title', 'content', 'author_note']


class FicAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'date', 'summary', 'author_note', 'pairing_type', 'rating', 'text_length', 'complete']

admin.site.register(Author)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Fic, FicAdmin)
