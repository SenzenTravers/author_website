from django.utils.translation import gettext, gettext_lazy as _

from django.contrib import admin
from .models import ExchangeParticipant, Prompt

class PromptAdmin(admin.ModelAdmin):
    fields = ['body', 'pairing_type', 'supporters']
    list_display = ('body', 'pairing_type')
    list_filter = ('body', 'pairing_type', 'supporters')


class ExchangeParticipantAdmin(admin.ModelAdmin):
    fields = ['member', 'likes', 'dislikes']
    list_display = ('member', 'likes', 'dislikes')
    list_filter = ('member', 'likes', 'dislikes')

admin.site.register(Prompt, PromptAdmin)
admin.site.register(ExchangeParticipant, ExchangeParticipantAdmin)
