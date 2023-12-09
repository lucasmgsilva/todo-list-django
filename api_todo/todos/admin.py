from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'edited_at', 'status')

admin.site.register(Todo, TodoAdmin)