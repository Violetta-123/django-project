from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Timetable


def index(request):
    return render(request, "main/Homepage.html")


def registration(request):
    if request.method == "POST":
        print("post")
        username = request.POST.get('username', None)
        # patient_patronymic = request.POST.get('patient_patronymic', None)
        # email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repeat_password = request.POST.get('repeat_password', None)
        if password != repeat_password:
            print('Пароли не совпадают!')
            return HttpResponseRedirect('/')

            try: user = authenticate(username=username, password=password)
            if user is not None:
                print('Такой пользователь уже существует')
            else: user = User.objects.create_user(username=username, password=password)

        except:  pass
    if username is None or password is None:
        return render(request, 'example_app/registration.html', locals())
    if request.user.is_autnenticated:
        return HttpResponseRedirect('/')
    return render(request, 'example_app/registration.html', locals())


# patient_date = request.POST.get('patient_date', None)
# policy = request.POST.get('policy', None)
# phone = request.POST.get('phone', None)


return render(request, "main/Reg.html")


def personal(request):
    return render(request, "main/PersonalArea.html")


def timetable(request):
    timetable = Timetable.objects.all()
    print(timetable)
    return render(request, "main/Timetable.html", {'timetable': timetable})
