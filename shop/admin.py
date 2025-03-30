from django.contrib import admin
from .models import Category, Product
# Regist`er your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name", "slug", "price",
        "available", "created", "updates",
    ]
    list_filter = ["available", "created", "price"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}