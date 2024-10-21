from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

    readonly_fields = ["image_tag"]
    fields = ["image", "image_tag"]

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 48px; height: 48px;" />'.format(
                    obj.image.url
                )
            )
        return "-"

    image_tag.short_description = "Resim"


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = ["name", "brand", "code", "isActive", "image_tag"]

    def image_tag(self, obj):
        if obj.images.exists():  # Use the related name "images"
            # Assuming there's at least one associated ProductImage
            return format_html(
                '<img src="{}" style="width: 48px; height: 48px;" />'.format(
                    obj.images.first().image.url  # Use the related name "images"
                )
            )
        return "-"

    image_tag.short_description = "Resim"


admin.site.register(Product, ProductAdmin)
