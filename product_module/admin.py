from django.contrib import admin

from . import models


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_filter = [
        'is_active',
        'category'
    ]
    list_display = [
        'title',
        'is_active',
        'is_delete',
        'price'
    ]
    list_editable = [
        'is_active',
        'price'
    ]


class AdminProductAccount(admin.ModelAdmin):
    list_filter = [
        'is_active',
        'is_delete'
    ]
    list_display = [
        'user_name',
        'passworld',
        'email',
        'ramz'
    ]


admin.site.register(models.Product, AdminProduct)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductAccount, AdminProductAccount)
