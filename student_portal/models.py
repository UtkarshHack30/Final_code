from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    link_url = models.CharField(max_length = 1000, blank=True)
    std = models.IntegerField()

    def __str__(self):
        return f"{self.link_url}-{self.std}"

    class Meta:
       ordering = ['std']


class Timetable(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    std = models.IntegerField()

    def __str__(self):
        return f"{self.std}-{self.image}"

    class Meta:
       ordering = ['std']



class Teacher(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #age = models.IntegerField()
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"


class Class(models.Model):
    std = models.IntegerField()
    subject = models.CharField(max_length=30)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"{self.std}-{self.subject}-{self.teacher}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    std = models.IntegerField()

    def __str__(self):
        return f"{self.user}-{self.std}"


class Announcements(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    mssg = models.TextField(null = True)

    def __str__(self):
        return f"{self.user}-{self.mssg}"




