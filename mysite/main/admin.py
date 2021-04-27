from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Cabinet)
admin.site.register(Doctor)
# admin.site.register(Day)
admin.site.register(Timetable)
admin.site.register(Patient)
admin.site.register(Record)