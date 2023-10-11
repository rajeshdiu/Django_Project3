
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myProject import views 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.signupPage,name="signupPage"), 
    path('loginPage', views.loginPage,name="loginPage"), 
    path('myAdmin/home', views.adminPage,name="adminPage"), 
    path('myAdmin/myProfile', views.myProfile,name="myProfile"), 
    path('profile/profileUpdate', views.profileUpdate,name="profileUpdate"), 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)