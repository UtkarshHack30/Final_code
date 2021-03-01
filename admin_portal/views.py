from django.shortcuts import get_object_or_404,render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from student_portal.forms import  UserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import authenticate, login, logout
from student_portal.models import Link, Timetable, Announcements


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.save()
            return HttpResponseRedirect(reverse('admin_portal:user_login'))
            
      
    else:
        user_form = UserForm()
        return render(request,'student_portal/signup.html',{'user_form':user_form})


class homeView(ListView):
    model = Link
    template_name = 'admin_portal/base.html' 
    queryset = Link.objects.all()

    def get_context_data(self, **kwargs):
        context = super(homeView , self).get_context_data(**kwargs)
        return context
    
class TimetableView(ListView):
    model = Timetable
    template_name = 'admin_portal/timetable.html' 
    queryset = Timetable.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TimetableView , self).get_context_data(**kwargs)
        return context
    

class UpdateLinkView(UpdateView):
    model = Link
    template_name="admin_portal/update.html"
    fields = ("link_url",)
    success_url = reverse_lazy("admin_portal:home")


class UpdateTTView(UpdateView):
    model = Timetable
    template_name="admin_portal/upload_tt.html"
    fields = ("image",)
    success_url = reverse_lazy("admin_portal:timetable")


class addNoticeView(CreateView):
    
    model = Announcements
    template_name = 'admin_portal/notice.html'
    fields = ('mssg',)
    success_url = reverse_lazy('admin_portal:notice')




def user_login(request):
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect(reverse("admin_portal:home"))
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ("invalid login details ")
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request,'admin_portal/registration/login.html')

    
 