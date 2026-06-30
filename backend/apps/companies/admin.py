from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'is_featured',
        'is_active'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    search_fields = ('name',)
    list_filter = (
        'category',
        'is_featured',
        'is_active'
    )