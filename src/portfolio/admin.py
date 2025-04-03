from django.contrib import admin

from .models import Project, ProjectCategory


# Register your models here.
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'description', 'category',
        'image', 'live_link', 'github_link',
        'created_at', 'updated_at'
    )
    list_filter = ('category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
