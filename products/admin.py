from django.contrib import admin

from .models import Product, Rate

class RateInline(admin.StackedInline):
    model = Rate

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [RateInline,]

