
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from myProject import views 
from myProject import staffViews 

urlpatterns = [
    path('admin', admin.site.urls), 
    path('', views.signupPage,name="signupPage"), 
    path('loginPage', views.loginPage,name="loginPage"), 
    path('myAdmin/home', views.adminPage,name="adminPage"), 
    path('myProfile/', views.myProfile,name="myProfile"), 
    path('profile/profileUpdate', views.profileUpdate,name="profileUpdate"), 
    path('profile/profileUpdate/ChangePassword', views.changePassword,name="changePassword"), 
    path('logoutPage', views.logoutPage,name="logoutPage"), 
    
    #Student Panel
    path('myAdmin/Student/addStudent', views.addStudent,name="addStudent"), 
    path('myAdmin/Student/studentList', views.studentList,name="studentList"), 
    path('myAdmin/Student/editStudent/<str:id>', views.editStudent,name="editStudent"), 
    path('myAdmin/Student/updateStudent', views.updateStudent,name="updateStudent"), 
    
    
    #Teacher Panel
    path('myAdmin/Teacher', views.addTeacher,name="addTeacher"), 
    path('myAdmin/Teacher/teacherList', views.teacherList,name="teacherList"), 
    path('myAdmin/Teacher/editTeacher/<str:id>', views.editTeacher, name="editTeacher"),
    path('myAdmin/Teacher/updateTeacher', views.updateTeacher,name="updateTeacher"), 
    
    #Department Panel
    path('myAdmin/Student/addDepartment', views.addDepartment,name="addDepartment"), 
    path('myAdmin/Student/departmentList', views.departmentList,name="departmentList"), 
    path('myAdmin/Student/editDepartment/<str:id>', views.editDepartment,name="editDepartment"), 
    path('myAdmin/Student/updateDepartment', views.updateDepartment,name="updateDepartment"), 
    
    #Subject Panel
    
    
    path('myAdmin/Subject/addSubject', views.addSubject,name="addSubject"), 
    path('myAdmin/Subject/subjectList', views.subjectList,name="subjectList"), 
    path('myAdmin/Subject/editSubject/<str:id>', views.editSubject,name="editSubject"),
    path('myAdmin/Subject/updateSubject', views.updateSubject,name="updateSubject"), 
    
    
    #Session Panel
    
    
    path('myAdmin/Session/addSession', views.addSession,name="addSession"), 
    path('myAdmin/Session/sessionList', views.sessionList,name="sessionList"), 
    path('myAdmin/Session/editSession/<str:id>', views.editSession,name="editSession"),
    path('myAdmin/Session/updateSession', views.updateSession,name="updateSession"), 
    
    
    
    
    #Teacher Views
    
    path('myTeacher/staffPage', views.staffPage,name="staffPage"), 
    
    
    #Student Views
    path('myStudent/studentPage', views.studentPage,name="studentPage"), 
    
    
    #Notification Page
    
    
    path('myAdmin/SentTeacherNotificationPage', views.SentTeacherNotification,name="SentTeacherNotification"), 
    path('myAdmin/saveTeacherNotification', views.saveTeacherNotification,name="saveTeacherNotification"), 
    
    
    
    #Teacher Urls
     path('Staff/myNotification', staffViews.myNotification,name="myNotification"), 
     path('Staff/markasDone/<str:status>', staffViews.markasDone,name="markasDone"), 
     
     
     
    #Apply for Leave
    
    path('myAdmin/Teacher/teacherleavePage', views.teacherleavePage,name="teacherleavePage"), 
     
    
     
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



