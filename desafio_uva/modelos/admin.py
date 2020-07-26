from django.contrib import admin

from .models import Processo

class ProcessoAdmin(admin.ModelAdmin):  #Display do modelo processo na página admin
    list_display = ['pasta', 'comarca', 'uf']
    ordering = ['pasta']

admin.site.register(Processo, ProcessoAdmin)