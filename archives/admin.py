from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import Author, Chapter, Fic


class ChapterAdmin(admin.ModelAdmin):
    fields = ['fic', 'title', 'number', 'content', 'author_note']


class FicAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'date', 'summary',
        'author_note', 'pairing_type', 'rating',
        'text_length', 'complete', 'visible'
        'clap']
    list_display = ('title', 'author', 'date', 'complete', 'visible', 'clap')
    list_filter = ('title', 'author', 'complete', 'visible')


admin.site.register(Author)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Fic, FicAdmin)
