from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def room(request, room_name):
    connection_type=request.path
    return render(request, "room.html", {"room_name": room_name})