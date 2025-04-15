from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import APIFic


# class ChapterAdmin(admin.ModelAdmin):
#     fields = ['fic', 'title', 'number', 'content', 'author_note']


class APIFicAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'date', 'summary',
        'author_note', 'pairing_type', 'rating',
        'text_length', 'complete', 'visibleByAdmin',
        'visibleByAuthenticatedOnly', 'clap']
    list_display = ('title', 'author', 'date', 'complete', 'visibleByAdmin', 'visibleByAuthenticatedOnly', 'clap')
    list_filter = ('title', 'author', 'complete', 'visibleByAdmin', 'visibleByAuthenticatedOnly')


# admin.site.register(Author)
# admin.site.register(Chapter, ChapterAdmin)
admin.site.register(APIFic, APIFicAdmin)
