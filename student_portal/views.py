from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import  UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.decorators import login_required
import csv
from .models import Student, Link, Timetable, Announcements
import os
from django.conf import settings

       

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.save()
            return HttpResponseRedirect(reverse('student_portal:user_login'))
            
      
    else:
        user_form = UserForm()
        return render(request,'student_portal/signup.html',{'user_form':user_form})



def user_login(request):
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect(reverse("student_portal:home", kwargs={"pk":request.user.id}))
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ("invalid login details ")
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'student_portal/registration/login.html')




class StudentHomeView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'student_portal/base.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
            context = super(StudentHomeView , self).get_context_data(**kwargs)
            current_student = Student.objects.get(user=self.request.user)
            context['student'] = current_student
            context['link'] = Link.objects.filter(std=current_student.std)[0]
            context['timetable'] = Timetable.objects.filter(std=current_student.std)[0]
            return context


class NoticeboardView(LoginRequiredMixin, ListView):
    model = Announcements
    template_name = 'student_portal/notice.html' 
    queryset = Announcements.objects.all()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
            context = super(NoticeboardView , self).get_context_data(**kwargs)
            current_student = Student.objects.get(user=self.request.user)
            context['student'] = current_student
            context['link'] = Link.objects.filter(std=current_student.std)[0]
            context['timetable'] = Timetable.objects.filter(std=current_student.std)[0]
            return context