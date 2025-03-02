from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "created_at","category")
    list_filter = ("created_at",)
    search_fields = ("name",)