from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import Author, Chapter, Fic, PairingType


class ChapterAdmin(admin.ModelAdmin):
    fields = ['fic', 'chapter_title', 'number', 'content', 'author_note']


class FicAdmin(admin.ModelAdmin):
    fields = ['author', 'fic_title', 'date', 'summary',
        'fic_author_note', 'pairing_type', 'rating',
        'text_length', 'complete', 'clap']
    list_display = ('fic_title', 'author', 'date', 'complete', 'clap')
    list_filter = ('fic_title', 'author', 'complete')

class PairingTypeAdmin(admin.ModelAdmin):
    fields = ['pairing_type']

admin.site.register(Author)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Fic, FicAdmin)
admin.site.register(PairingType, PairingTypeAdmin)
