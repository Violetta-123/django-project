from django.conf.urls import url
from django.urls import path
from . import views
from .views import SignUpView, LoginUser

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', LoginUser.as_view(), name='login'),
    path('personal', views.personal, name='personal'),
    path('timetable', views.timetable, name='timetable'),
    path('signup', SignUpView.as_view(), name='signuup'),
]