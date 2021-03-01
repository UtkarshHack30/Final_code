
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student_Portal/', include('student_portal.urls')),
    path('Admin_Portal/', include('admin_portal.urls')),
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
