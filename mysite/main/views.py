from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from pip._vendor.requests import post
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page
from .forms import MyUserCreationForm, UserInfoForm, MyLoginUserForm
from .models import Timetable, Patient
from django.contrib.auth.models import User


@cache_page(60 * 3)
def index(request):
    form_class = MyLoginUserForm
    form_class1 = MyUserCreationForm
    return render(request, "main/Homepage.html", {'form_class': form_class, 'form_class1': form_class1})

@cache_page(60 * 3)
def registration(request):
    if request.method == "POST":
        print("post")
    form_class = MyUserCreationForm
    return render(request, "registration/signup.html", {'form_class': form_class})

    #     if request.method == "POST":
    #         print("post")
    #         username = request.POST.get('username', None)
    #         # patient_patronymic = request.POST.get('patient_patronymic', None)
    #         # email = request.POST.get('email', None)
    #         password = request.POST.get('password', None)
    #         repeat_password = request.POST.get('repeat_password', None)
    #         if password != repeat_password:
    #             print('Пароли не совпадают!')
    #             return HttpResponseRedirect('/')
    #
    #             try: user = authenticate(username=username, password=password)
    #             if user is not None:
    #                 print('Такой пользователь уже существует')
    #             else: user = User.objects.create_user(username=username, password=password)
    #
    #         except:  pass
    #     if username is None or password is None:
    #         return render(request, 'example_app/registration.html', locals())
    #     if request.user.is_autnenticated:
    #         return HttpResponseRedirect('/')
    #     return render(request, 'example_app/registration.html', locals())

    # patient_date = request.POST.get('patient_date', None)
    # policy = request.POST.get('policy', None)
    # phone = request.POST.get('phone', None)


class LoginUser(LoginView):
    form_class = MyLoginUserForm
    template_name = 'registration/login.html'


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


    def post(self, request, *args, **kwargs):
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
            )
        return HttpResponseRedirect('/')


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'registration/login.html'

@cache_page(60 * 3)
def personal(request):
    return render(request, "main/PersonalArea.html")

@cache_page(60 * 3)
def timetable(request):
    timetable = Timetable.objects.all()
    print(timetable)
    return render(request, "main/Timetable.html", {'timetable': timetable})


@login_required
@cache_page(60 * 3)
def personal(request):
    form = UserInfoForm(request.POST)
    if request.method == "POST" and form.is_valid():
        info = form.save(commit=False)
        info.post = post
        info.user = request.user
        info.save()
    return render(request, 'main/PersonalArea.html', {'form': form})  # locals()
