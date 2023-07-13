from django.contrib import admin
from home.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ["original_url", "short_url", "created_date"]

    class Meta:
        model = ShortURL
