from django.db import models
from .utils import create_short_url


class ShortURL(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    original_url = models.URLField(max_length=256)
    short_url = models.CharField(max_length=7, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)
        super().save(*args, **kwargs)