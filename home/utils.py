from django.conf import settings
from random import choice
from string import ascii_letters, digits
from . import models

SIZE = getattr(settings, "SHORT_URL_LENGTH", 7)
CHARS = ascii_letters + digits


def create_random_code(chars=CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_short_url(obj):
    random_code = create_random_code()
    if models.ShortURL.objects.filter(short_url=random_code).exists():
        return create_short_url(obj)
    return random_code