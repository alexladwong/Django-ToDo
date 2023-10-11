from django.contrib import admin
from .models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at', 'created_by')
    search_fields = ('task', 'created_by',)
admin.site.register(Task, TaskAdmin)