from django.contrib import admin
from .models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "created_at", "deadline", "is_done")
    list_filter = ("is_done", "deadline", "tags")
    search_fields = ("content",)
    date_hierarchy = "created_at"
    filter_horizontal = ("tags",)
