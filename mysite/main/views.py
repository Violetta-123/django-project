from django.shortcuts import render
from django.http import HttpResponse

from .models import Timetable


def index(request):
    return render(request, "main/Homepage.html")


def registration(request):
    return render(request, "main/Reg.html")


def personal(request):
    return render(request, "main/PersonalArea.html")

def timetable(request):
    timetable = Timetable.objects.all()
    print(timetable)
    return render(request, "main/Timetable.html", {'timetable': timetable})