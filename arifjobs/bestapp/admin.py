from django.contrib import admin
from bestapp.models import Hydjobs,Bngjobs,Punejobs
# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','elegiblity','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)
class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','elegiblity','address','email','phonenumber']
admin.site.register(Punejobs,PunejobsAdmin)
class BngjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','elegiblity','address','email','phonenumber']
admin.site.register(Bngjobs,BngjobsAdmin)