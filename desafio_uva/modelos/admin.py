from django.contrib import admin

from .models import Processo

class ProcessoAdmin(admin.ModelAdmin):
    list_display = ['pasta', 'comarca', 'uf']
    ordering = ['pasta']

admin.site.register(Processo, ProcessoAdmin)