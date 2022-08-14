from django.contrib import admin
from app.models import *
from django.utils.safestring import mark_safe


@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    list_display = [
        "image", 
        "libele", 
        "created",
        "updated",
        "is_active"
        ]
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')

@admin.register(Site)
class AdminSite(admin.ModelAdmin):
    list_display = [
        "image",
        "name", 
        "email", 
        "phone", 
        "copyright",
        "created",

        "updated",
        "is_active"
        ]
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')

@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = [
    "image",
    "name", 
    "libele",
    "description",
    "order",  
    "created",
    "updated",
    "is_active"
    ]
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')
    
@admin.register(UnderService)
class AdminUnderService(admin.ModelAdmin):
    list_display = [
        "image",
        "name", 
        "libele",
        "description",
        "order", 
 
        "created",
        "updated",
        "is_active"
        ]
    def image(self, obj): 
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:200px">')
@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = [ 
        "description",
 
        "created",
        "updated",
        "is_active"
    ]
@admin.register(ReseauSocial)
class AdminReseauSocial(admin.ModelAdmin):
    list_display = [ 
        "name",
        "icon", 
        "link",
 
        "created",
        "updated",
        "is_active"
    ]