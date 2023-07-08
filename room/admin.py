from django.contrib import admin
from room.models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Message)

