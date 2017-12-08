from django.shortcuts import render
from django.http import HttpResponse


def getAll(request) :
    return HttpResponse("1) Skyrim\n2) GOT\n3) Requiem for a Dream\n4) Zelda")

def get(request, music_id) :
    if music_id == "1":
        return HttpResponse("Skyrim")
    elif music_id == "2":
        return HttpResponse("GOT")
    elif music_id == "3":
        return HttpResponse("Requiem for a Dream")
    elif music_id == "4":
        return HttpResponse("Zelda")
    else:
        return HttpResponse("No such song")
