from django.contrib import admin

from .models import SocialResource, MenuItem


class SocialResourceAdmin(admin.ModelAdmin):
    list_display = ("order_id", "name", "title", )
    ordering = ("order_id", )


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("order_id", "label", "uri", )
    ordering = ("parent", "order_id", )


admin.site.register(SocialResource, SocialResourceAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
