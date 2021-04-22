from django.contrib import admin

from .models import Project,UserTasks

# Register your models here.
admin.site.register(Project)
admin.site.register(UserTasks)
