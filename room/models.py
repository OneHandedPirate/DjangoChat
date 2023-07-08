from django.db import models
from core.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    password = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_at',)

    def __str__(self):
        return f'{self.content} - {self.added_at}'
