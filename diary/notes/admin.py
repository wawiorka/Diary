from django.contrib import admin

from .models import Note

# Register your models here.
# admin.site.register(Note)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)