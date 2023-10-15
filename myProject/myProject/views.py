from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myApp.models import *
from django.contrib import messages
from myApp import EmailBackEnd
from django.contrib.auth import login as auth_login


def signupPage(request):
    error_messages = {
        'password_error': 'Password and Confirm Password not match',
    }
    if request.method == "POST":
        uname = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirmpassword")

        if pass1!= pass2:
             messages.error(request, error_messages['password_error'])
        else:
            # Use your customUser model to create a user
            myuser = customUser.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            return redirect("loginPage")

    # messages.success(request, 'Signup successful.')
    return render(request, "signup.html")

def logoutPage(request):
    logout(request)
    return redirect("loginPage")

def loginPage(request):
    error_messages = {
        'username_error': 'Username is required.',
        'password_error': 'Password is required.',
        'login_error': 'Invalid username or password. Please try again.',
    }

    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("password")
        
        if not username:
            messages.error(request, error_messages['username_error'])
        elif not pass1:
            messages.error(request, error_messages['password_error'])
        else:
            user = EmailBackEnd.authenticate(request, username=username, password=pass1,)

            if user is not None:
                login(request,user)
                user_type = user.user_type
                if user_type == '1':
                    return redirect("adminPage")
                elif user_type == '2':
                    return render(request, "Staff/staffhome.html")
                elif user_type == '3':
                    return render(request, "Students/Stustudenthome.html")
                else:
                    return redirect("signupPage")
            else:
                messages.error(request, error_messages['login_error'])

    return render(request, "login.html")


def adminPage(request):
    
    return render(request,"myAdmin/adminhome.html")


def myProfile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

from django.contrib.auth.hashers import check_password

def profileUpdate(request):
    error_messages = {
        'success': 'Profile Update Successfully',
        'error': 'Profile Not Updated',
        'password_error': 'Current password is incorrect',
    }
    
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        password = request.POST.get("password")
        username = request.POST.get("username")
        email = request.POST.get("email")
        
        try:
            cuser = customUser.objects.get(id=request.user.id)
            
            cuser.first_name = firstname
            cuser.last_name = lastname
            cuser.profile_pic = profile_pic
            
            # Verify the current password provided matches the user's current password
            if not cuser.check_password(password):
                messages.error(request, error_messages['password_error'])
            else:
                # If the current password is correct, proceed to update other fields
                if profile_pic is not None:
                    cuser.profile_pic = profile_pic
                
                # You can add additional fields to update here as needed

                cuser.save()
                auth_login(request, cuser)
                messages.success(request, error_messages['success'])
                return redirect("profileUpdate")
        except:
            messages.error(request, error_messages['error'])
    
    return render(request, 'profile.html')


# views.py

def changePassword(request):
    error_messages = {
        'success': 'Changed Successfully',
        'mismatch': 'New password and confirm password not matched',
        'old_password': 'Old password not match',
    }
    
    if request.method == "POST":
        old_password = request.POST.get("oldPassword")
        new_password = request.POST.get("newpassword")
        confirm_password = request.POST.get("confirmPassword")
        user = request.user
        
        if user.check_password(old_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, error_messages['success'])
                return redirect("loginPage")
            else:
                messages.error(request, error_messages['mismatch'])
        else:
            messages.error(request, error_messages['old_password'])

    return render(request, "changepassword.html")



def addStudent(request):
    error_messages = {
        'success': 'Student Add Successfully',
        'error': 'Student Add Failed',
    }
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # Changed from 'user_name' to 'username'
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("courseid")
        session_year_id = request.POST.get("sessionyearid")

        # Check if email or username already exists
        if customUser.objects.filter(email=email).exists() or customUser.objects.filter(username=username).exists():
            messages.error(request, error_messages['error'])
        else:
            # Create the customUser instance
            user = customUser.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic
            user.user_type = 3  # Assuming '3' represents students

            # Save the user instance
            user.save()

            # Retrieve the selected course and session year
            myCourse = courseModel.objects.get(id=course_id)
            mySessionYear = sessionYearModel.objects.get(id=session_year_id)

            # Create the student instance
            student = studentModel(
                admin=user,
                address=address,
                sessionyearid=mySessionYear,
                courseid=myCourse,
                gender=gender,
            )

            # Save the student instance
            student.save()

            messages.success(request, error_messages['success'])
            return redirect("addStudent")

    # Fetch the course and session year data to display in the form
    course = courseModel.objects.all()
    session_year = sessionYearModel.objects.all()
    st=studentModel.objects.all()
    context = {
        "course": course,
        "session": session_year,
        "st":st,   
    }

    return render(request, "myAdmin/addStudent.html", context)

def studentList(request):
    
    allStudent=studentModel.objects.all()
    print(allStudent)
    
    return render(request,"myAdmin/studentlist.html",{"student":allStudent})

def editStudent(request,id):
    student=studentModel.objects.filter(id=id)
    course = courseModel.objects.all()
    session_year = sessionYearModel.objects.all()
    st=studentModel.objects.all()
    context = {
        "course": course,
        "session": session_year,
        "student":student,
        
    }
    
    return render(request,"myAdmin/editStudent.html",context)

def addTeacher(request):
    error_messages = {
        'success': 'Teacher Add Successfully',
        'erroremail': 'email already exist',
        'errorusername': 'username already exist',
    }
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")  # Changed from 'user_name' to 'username'
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        course_id = request.POST.get("courseid")
        mobile = request.POST.get("mobile")
        experience = request.POST.get("experience")

        # Check if email or username already exists
        if customUser.objects.filter(email=email).exists():
            messages.error(request, error_messages['erroremail'])
        if customUser.objects.filter(username=username).exists():
            messages.error(request, error_messages['errorusername'])
        else:
            # Create the customUser instance
            user = customUser.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic
            user.user_type = 2  # Assuming '2' represents students

            # Save the user instance
            user.save()

            # Retrieve the selected course and session year
            myCourse = courseModel.objects.get(id=course_id)

            # Create the student instance
            teacher = teacherModel(
                admin=user,
                address=address,
                courseid=myCourse,
                gender=gender,
                mobile=mobile,
                experience=experience,
            )

            # Save the student instance
            teacher.save()

            messages.success(request, error_messages['success'])
            return redirect("addTeacher")

    # Fetch the course and session year data to display in the form
    course = courseModel.objects.all()
    st=teacherModel.objects.all()
    context = {
        "course": course,
    }

    return render(request, "myAdmin/addTeacher.html", context)


def teacherList(request):
    
    allTeacher=teacherModel.objects.all()
    print(allTeacher)
    
    return render(request,"myAdmin/teacherList.html",{"teacher":allTeacher})


def editTeacher(request,id):
    teacher=teacherModel.objects.filter(id=id)
    course = courseModel.objects.all()
    context = {
        "course": course,
        "teacher":teacher,
    }
    
    return render(request,"myAdmin/editTeacher.html",context)