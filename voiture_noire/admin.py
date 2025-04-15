from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import Prompt

class PromptAdmin(admin.ModelAdmin):
    fields = ['body', 'pairing_type', 'supporters']
    list_display = ('body', 'pairing_type')
    list_filter = ('body', 'pairing_type', 'supporters')


# admin.site.register(Author)
# admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Prompt, PromptAdmin)
