from django.contrib import admin

from .models import Unit, Section, Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ("section", "unit", "order_id", )


class UnitAdmin(admin.ModelAdmin):
    list_display = ("token", "title", "annotation", "body", "is_active", )


class SectionAdmin(admin.ModelAdmin):
    list_display = ("label", "bg_image", "is_active", "updated", )


admin.site.register(Content, ContentAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Section, SectionAdmin)
