from django.contrib import admin
from clothing.models import cloth
# Register your models here.



class clothadmin(admin.ModelAdmin):  
    list_display = ('model','size','value','amount','category')
    search_fields = ('model','size','value','amount','category')


admin.site.register(cloth,clothadmin)
