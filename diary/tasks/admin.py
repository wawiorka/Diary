from django.contrib import admin

from .models import Task, Goal

# Register your models here.
# admin.site.register(Task)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

# admin.site.register(Goal)
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)