from django.contrib import admin
from .models import Task
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'created_at']
    list_filter = ['created_at', 'is_done']



admin.site.register(Task, TaskAdmin)