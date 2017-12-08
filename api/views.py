from django.shortcuts import render
from django.http import HttpResponse


def getAll(request) :
    return HttpResponse("Skyrim\nGOT\nRequiem for a Dream\nZelda")

def get(request) :
    return "Not implemented yet"
