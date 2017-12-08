from django.contrib import admin

from .models import Unit, Section, Content


def admin_method_attrs(**outer_kwargs):
    """
    Wrap an admin method with passed arguments as attributes and values.
    (common admin manipulation such as setting  short_description, etc.)
    """
    def method_decorator(func):
        for kw, arg in outer_kwargs.items():
            setattr(func, kw, arg)
        return func
    return method_decorator


def shorten_string(val, num):
    if val:
        if len(val) > num:
            return val[:num] + "..."
    return val



class ContentAdmin(admin.ModelAdmin):
    list_display = ("section", "column", "order_id", "unit", )
    ordering = ("section", "column", "order_id", )
    list_filter = ("section", "column", )


class UnitAdmin(admin.ModelAdmin):
    @admin_method_attrs(short_description='active',
                        admin_order_field='is_active',
                        boolean=True)
    def _is_active(self, obj):
        return obj.is_active

    @admin_method_attrs(admin_order_field='body')
    def _body(self, obj):
        return shorten_string(obj.body, 100)

    @admin_method_attrs(admin_order_field='annotation')
    def _annotation(self, obj):
        return shorten_string(obj.annotation, 30)

    list_display = ("token", "_is_active", "title", "_annotation", "_body", )
    ordering = ("token", )
    search_fields = ("annotation", "body", )


class SectionAdmin(admin.ModelAdmin):
    list_display = ("label", "bg_image", "is_active", "updated", )


admin.site.register(Content, ContentAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Section, SectionAdmin)
