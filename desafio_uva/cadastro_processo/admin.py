import csv
from django.contrib import admin

from .models import Planilha
from modelos.models import Processo


def cadastro(modeladmin, request, queryset):  #Ação para cadastro dos processos
    for planilha in queryset:   #iteração das planilhas selecionadas
        csv_data = csv.DictReader(open(planilha.arquivo.path, 'r'), delimiter=';')  #leitura dos dados da planilha
        for linha in csv_data:  # cadastro dos processos
            Processo.objects.get_or_create(
                pasta   = linha['pasta'],
                comarca = linha['comarca'],
                uf      = linha['uf'],
            )
cadastro.short_description = 'Cadastrar processos'

class PlanilhaAdmin(admin.ModelAdmin):  #Display do modelo planilha na página admin
    list_display = ['nome', 'cliente', 'arquivo']
    ordering = ['nome']
    actions = [cadastro]    #Permissão para que a ação de cadastro seja efetuada no modelo

admin.site.register(Planilha, PlanilhaAdmin)
