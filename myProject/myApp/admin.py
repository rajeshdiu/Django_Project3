from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin


class userModel(UserAdmin):
    list_display=["username","user_type"]

admin.site.register(customUser,userModel)

admin.site.register(courseModel)
admin.site.register(sessionYear)
admin.site.register(studentModel)