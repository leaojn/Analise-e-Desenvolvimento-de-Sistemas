from django.contrib import admin
from core.models import Jogador
# Register your models here.
@admin.register(Jogador)
class PoloAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">home</i>'
    list_display = ('nome',)
    ordering = ['nome']
    fieldsets = (
        (None, {
            'fields': ('nome','altura','nacionalidade','image','idade')
        }),
    )
