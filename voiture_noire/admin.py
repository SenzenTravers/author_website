from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import DiscordProfile, Prompt

class PromptAdmin(admin.ModelAdmin):
    fields = ['body', 'pairing_type', 'supporters']
    list_display = ('body', 'pairing_type')
    list_filter = ('body', 'pairing_type', 'supporters')


class DiscordProfileAdmin(admin.ModelAdmin):
    fields = ['member', 'likes', 'dislikes']
    list_display = ('member', 'likes', 'dislikes')
    list_filter = ('member', 'likes', 'dislikes')

# admin.site.register(Author)
# admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Prompt, PromptAdmin)
admin.site.register(DiscordProfile, DiscordProfileAdmin)