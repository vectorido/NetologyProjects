from django.contrib import admin

from .models import Product, Stock, StockProduct


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


class StockAdmin(admin.ModelAdmin):
    inlines = [StockProductInline]
    list_display = ['address']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)