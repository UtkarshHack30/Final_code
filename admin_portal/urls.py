from django.urls import path, include
from . import views
from student_portal.forms import CustomAuthForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'admin_portal'

urlpatterns = [

    path('signup',views.signup, name='signup'),
    path('login', views.user_login, name='user_login'),
    path('home/', include('django.contrib.auth.urls'),name="logout"),
    path('home',views.homeView.as_view(), name='home'),
    path('class_links/<int:pk>/upload', views.UpdateLinkView.as_view(), name='upload_link' ),
    #path('timetable/<int:pk>/upload', views.UpdateTimetableView.as_view(), name='tt_upload_link' ),
    path('timetable',views.TimetableView.as_view(), name='timetable'),
    path('timetable/<int:pk>/upload',views.UpdateTTView.as_view(), name='update_tt'),
    path('announcements',views.addNoticeView.as_view(), name='notice'),


] 