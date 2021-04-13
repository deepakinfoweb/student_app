from django.contrib import admin

# Register your models here.
from studentinfo.models import *

admin.site.register(users)
admin.site.register(marks)
admin.site.register(student)