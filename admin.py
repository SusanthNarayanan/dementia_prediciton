from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'Age', 'EDUC', 'SES','MMSE','eTIV','nWBV','ASF','predictions')


admin.site.register(Data, DataAdmin)
