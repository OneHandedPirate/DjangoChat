from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    if room.password:
        if request.method == 'GET':
            return render(request, 'room/checkRoomPassword.html')
        elif request.method == 'POST':
            if not room.check_password(request.POST.get('password')):
                return render(request, 'room/checkRoomPassword.html',
                              {'error': 'Invalid password, please try again'})

    messages = Message.objects.filter(room=room)[:25:-1]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})