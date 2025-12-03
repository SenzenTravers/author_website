from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import DiscordProfile, Prompt, ServerEvent

class PromptAdmin(admin.ModelAdmin):
    fields = ['body', 'pairing_type', 'supporters']
    list_display = ('body', 'pairing_type')
    list_filter = ('body', 'pairing_type', 'supporters')


class DiscordProfileAdmin(admin.ModelAdmin):
    fields = ['member', 'likes', 'dislikes', 'is_creator', 'birthday']
    list_display = ('member', 'likes', 'dislikes', 'is_creator', 'birthday')
    list_filter = ('member', 'likes', 'dislikes', 'is_creator', 'birthday')


class ServerEventAdmin(admin.ModelAdmin):
    fields = ['actor', 'event_type', 'title', 'event_start', 'event_end']
    list_display = ('actor', 'event_type', 'title', 'event_start', 'event_end')
    list_filter = ('actor', 'event_type', 'title', 'event_start', 'event_end')

admin.site.register(Prompt, PromptAdmin)
admin.site.register(DiscordProfile, DiscordProfileAdmin)
admin.site.register(ServerEvent, ServerEventAdmin)