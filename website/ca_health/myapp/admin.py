from django.contrib import admin

# Register your models here.
from django.conf import settings

from django.contrib import admin

from .models import Inpatient, Infection, Food_Desert, Demographic

class Food_DesertAdmin(admin.ModelAdmin):
    list_display = ('county', 'n_tracts', 'n_urban', 'n_rural', 'pop2010', 'num_fd')
    search_fields = ('county','num_fd')
    ordering = ['county', 'pop2010','num_fd','n_urban','n_rural','n_tracts']

class DemographicAdmin(admin.ModelAdmin):
    list_display = ('county', 'pct_white', 'pct_black', 'pct_hspnc', 'pct_asian', 'pct_65over')
    search_fields = ('county','pct_white')
    ordering = ['county', 'pct_white', 'pct_black', 'pct_hspnc', 'pct_asian', 'pct_65over']

class InpatientAdmin(admin.ModelAdmin):
    list_display = ('county', 'mort_30_hf', 'readm_30_hf', 'std', 'hiv')
    search_fields = ('county','HIV')
    ordering = ['county', 'mort_30_hf', 'readm_30_hf', 'std', 'hiv']

admin.site.register(Food_Desert, Food_DesertAdmin)
admin.site.register(Demographic, DemographicAdmin)
admin.site.register(Inpatient, InpatientAdmin)
admin.site.register(Infection)
