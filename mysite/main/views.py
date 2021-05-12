from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/Homepage.html")


def registration(request):
    return render(request, "main/Reg.html")


def personal(request):
    return render(request, "main/PersonalArea.html")

def timetable(request):
    return render(request, "main/Timetable.html")