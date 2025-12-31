from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


def register_method(request):
   
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        # print(username,email,password,confirm)
        if not username:
            errors['username'] = "Username is Required"
        elif User.objects.filter(username=username).exists():
            errors['username'] = "Username already exists !! user another"

        if not email:
            errors['email'] = "Email field is Required"
        elif User.objects.filter(email=email).exists():
            errors['email'] = "Email already exists ! user another email"
        
        if not password:
            errors['password'] = "Password is required"
        elif len(password) <=6:
            errors['password']= "Password contains more than 6 characters"

        if not confirm:
            errors['confirm'] = " Confirm Password is required"

        if password != confirm:
            errors['confirm'] = "Confirm password not matched !!"

        if errors:
            return render(request,'auth/register_page.html',{'errors':errors,'data':request.POST})
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
            messages.success(request,'User Registration Successfully !! ')
            return redirect('login') 
    else:
        return render(request,'auth/register_page.html')


# def login_method(request):
#     errors = {}

#     if request.method == 'POST':
#         username= request.POST.get('username')
#         password = request.POST.get('password')

#         if not username:
#             errors['username'] = "Username is Required"
#         elif not User.objects.filter(username=username).exists():
#             errors['username'] = "Username doesn't exists"


#         if not password:
#             errors['password'] = "Password is Required"

#         # authenticate(request, username=username,password=password)
#         # select username from User where email=email;
#         if not errors:
#             user = authenticate(request,username=username,password=password)
#             if user is not None:
#                 # session generate garxa 
#                 login(request,user)
#                 messages.success(request,'User logged in successfully')
#                 return redirect('index')
#             else:
#                 errors['password'] = "Password is incorrect"
#                 return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})
#         else:
#             return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})

#     return render(request,'auth/login_page.html')



def login_method(request):
    
    errors = {}

    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            errors['email'] = "Email is Required"
        
        if not User.objects.filter(email=email).exists():
            errors['email'] = "Email doesn't exists"

        if not password:
            errors['password'] = "Password is Required"

        if not errors:
            check_user = User.objects.get(email=email)
            user = authenticate(request,username=check_user.username,password=password)
            if user is not None:
                
                login(request,user)
                messages.success(request,'User logged in successfully')
                return redirect('index')
            else:
                errors['password'] = "Password is incorrect"
                return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})
        else:
            return render(request,'auth/login_page.html',{'errors':errors,'data':request.POST})

    return render(request,'auth/login_page.html')