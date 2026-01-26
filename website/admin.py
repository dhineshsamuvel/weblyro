from django.contrib import admin
from .models import Lead, Project, CMSContent


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "status", "created_at")
    list_filter = ("service", "status", "created_at")
    search_fields = ("name", "email", "phone", "company", "message")
    list_editable = ("status",)
    list_per_page = 25
    ordering = ("-created_at",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "website_url", "created_at")
    search_fields = ("title", "client", "services")
    ordering = ("-created_at",)


@admin.register(CMSContent)
class CMSContentAdmin(admin.ModelAdmin):
    list_display = ("page", "key", "value")
    list_filter = ("page",)
    search_fields = ("key", "value")
    list_per_page = 50
