from django.contrib import admin
from .models import Lead, Project, CMSContent


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "status", "created_at")

    # safe filters
    list_filter = ("service", "status")

    # remove TextField (message) from search to avoid admin hang
    search_fields = ("name", "email", "phone", "company")

    # editable field must NOT be in list_display before non-editable fields
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
    search_fields = ("key",)
    list_per_page = 50
