from django.contrib import admin

from cadastro.models import Pessoa

# Register your models here.
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass
