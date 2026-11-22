from django.contrib import admin
from .models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'level', 'work_mode', 'is_featured', 'is_active', 'created_at')
    list_filter = ('level', 'work_mode', 'employment_type', 'is_featured', 'is_active')
    search_fields = ('title', 'company__name', 'skills', 'location')
    list_editable = ('is_featured', 'is_active')
