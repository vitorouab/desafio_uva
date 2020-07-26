import csv
from django.contrib import admin

from .models import Planilha
from modelos.models import Processo

def cadastro(modeladmin, request, queryset):
    for planilha in queryset:
        csv_data = csv.DictReader(open(planilha.arquivo.path, 'r'), delimiter=';')
        for linha in csv_data:
            Processo.objects.get_or_create(
                pasta   = linha['pasta'],
                comarca = linha['comarca'],
                uf      = linha['uf'],
            )
cadastro.short_description = 'Cadastrar processos'

class PlanilhaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cliente', 'arquivo']
    ordering = ['nome']
    actions = [cadastro]

admin.site.register(Planilha, PlanilhaAdmin)
