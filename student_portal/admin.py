from django.contrib import admin
from .models import Class, Link, Teacher, Timetable, Student, Announcements
# Register your models here.

admin.site.register(Class)
admin.site.register(Link)
admin.site.register(Teacher)
admin.site.register(Timetable)
admin.site.register(Student)
admin.site.register(Announcements)