from django.contrib import admin
from room.models import Room, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'room', 'user', 'added_at')
    list_filter = ('room', 'user')
    ordering = ('-added_at',)


admin.site.register(Message, MessageAdmin)

