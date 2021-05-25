from django.contrib import admin
from .models import Data, Search

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display = ('country', 'population', 'latitude', 'longtitude')


admin.site.register(Search)
admin.site.register(Data, DataAdmin)