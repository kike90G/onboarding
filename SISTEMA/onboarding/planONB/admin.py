from django.contrib import admin
from .models import  Ontactitud, Ontactividad, Ontasignacion, Ontcumple, Ontcumpleactitud, Ontcumpleactividad , Ontdepartamento ,Ontempleado, Onthabilidad, Ontnivel, Ontplan, Ontplanactitud, Ontplanactividad, Ontpuesto, Ontstatusempleado, Ontstatuspuesto, Onttipo

admin.site.site_header = 'Administración Onboarding'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Onboarding'


class ActitudAdmin(admin.ModelAdmin):
    list_display = ('actitudid', 'will', 'descripcion', 'peso')
    ordering = ('will',)
    search_fields = ('actitudid', 'will', 'descripcion',)
    list_editable = ('will','descripcion', 'peso')

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('actividadid', 'descripcion')
    ordering = ('descripcion',)
    search_fields = ('actividadid', 'descripcion',)
    list_editable = ('descripcion',)

class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('asignacionid', 'descripcion')
    ordering = ('descripcion',)
    search_fields = ('asignacionid', 'descripcion',)
    list_editable = ('descripcion',)

class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipoid', 'descripcion')
    ordering = ('descripcion',)
    search_fields = ('tipoid', 'descripcion',)
    list_editable = ('descripcion',)

class CumpleAdmin(admin.ModelAdmin):
    list_display = ('cumpleid', 'descripcion', 'porcentaje', 'tipoid')
    ordering = ('descripcion',)
    search_fields = ('cumpleid', 'descripcion',)
    list_editable = ('descripcion', 'porcentaje', 'tipoid',)       


# Register your models here.
admin.site.register(Ontactitud, ActitudAdmin)
admin.site.register(Ontactividad, ActividadAdmin)
admin.site.register(Ontasignacion, AsignacionAdmin)
admin.site.register(Ontcumple, CumpleAdmin)
admin.site.register(Ontcumpleactitud)
admin.site.register(Ontcumpleactividad)
admin.site.register(Ontdepartamento)
admin.site.register(Ontempleado)
admin.site.register(Onthabilidad)
admin.site.register(Ontnivel)
admin.site.register(Ontplan)
admin.site.register(Ontplanactitud)
admin.site.register(Ontplanactividad)
admin.site.register(Ontpuesto)
admin.site.register(Ontstatusempleado)
admin.site.register(Ontstatuspuesto)
admin.site.register(Onttipo, TipoAdmin)



