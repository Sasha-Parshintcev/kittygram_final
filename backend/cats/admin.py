from django.contrib import admin

from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'color', 'birth_year', 'owner', 'achievements', 'image'
    )


admin.site.register(Cat, CatAdmin)
