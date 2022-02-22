

from django.contrib import admin

from task.models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    list = ('title','description','completed')

admin.site.register(Task,TaskAdmin)
admin.site.register(Category)