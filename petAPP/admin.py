from django.contrib import admin
from petAPP.models import *
# Register your models here.
class petAdmin(admin.ModelAdmin):
    list_display=['gender','image','species','name','breed','age','gender','description','price']
admin.site.register(petstore,petAdmin)
