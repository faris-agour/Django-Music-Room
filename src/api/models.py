import random
import string

from django.db import models


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=55, unique=True)
    votes_to_skip = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)


def generate_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_letters, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

