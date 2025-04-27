from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import Author, Chapter, Fic, PairingType


class ChapterAdmin(admin.ModelAdmin):
    fields = ['fic', 'chapter_title', 'number', 'content', 'author_note']


class FicAdmin(admin.ModelAdmin):
    fields = ['author', 'fic_title', 'date', 'summary',
        'fic_author_note', 'pairing_type', 'rating',
        'visible', 'visible_not_member_only',
        'text_length', 'complete', 'clap',
        'pairing_archetype', 'one_sentence_summary']
    list_display = ('fic_title', 'author', 'date', 'complete', 'clap')
    list_filter = ('fic_title', 'author', 'complete', 'visible', 'visible_not_member_only')

class PairingTypeAdmin(admin.ModelAdmin):
    fields = ['pairing_type', 'label']

admin.site.register(Author)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Fic, FicAdmin)
admin.site.register(PairingType, PairingTypeAdmin)
