"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from studentinfo.api.studnetAPI import login,home,Addnewstudent,DeleteStudent,EditStudentName,logout

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',login, name='login'),
    url(r'^home$',home, name='home'),
    url(r'^addnewstudent$',Addnewstudent.as_view(), name='addnewstudent'),
    url(r'^delete_student$',DeleteStudent.as_view(), name='delete_student'),
    url(r'^edit_student_name$',EditStudentName.as_view(), name='edit_student_name'),
    url(r'^logout$',logout, name='logout'),
]
