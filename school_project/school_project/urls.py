from django.contrib import admin
from django.urls import path
from students.views import home, student_list, student_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('students/', student_list),
    path('students/<int:id>/', student_detail),
]