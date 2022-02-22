

from django.contrib import admin

from task.models import Task


class TaskAdmin(admin.ModelAdmin):
    list = ('title','description','completed')

admin.site.register(Task,TaskAdmin)