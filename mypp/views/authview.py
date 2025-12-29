from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


def register_method(request):
    errors={}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        
        if not username:
            errors["username"]="username hal na mula"
        elif User.objects.filter(username=username).exists():
            errors["username"]="useralready exists"
        if not email:
            errors['email']='email chai kasla la halcha'
        elif User.objects.filter(email=email).exists():
              errors["email"]="email already exists"
        if not password:
            errors['password']='daju halnu na password feri hacker la tanab dincha'
        elif len(password)<=6:
            errors['password']="password contains less then 6 character"
        if not confirm:
            errors["confirm"]="confirm hannu na daju"
        if password != confirm:
            errors['confirm'] = "aakha ho ki guccha password aaautai vayana ni"

        if errors:
            return render(request,'auth/register_page.html',{'errors':errors,'data':request.POST})
        else:
            user = User.objects.create(
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            messages.success(request,"user registration successfully")
            return redirect('login')
    else:
        return render(request,'auth/register_page.html')

def login_method(request):
    errors = {}

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username:
            errors['username'] = 'Username is required'
        if not password:
            errors['password'] = 'Password is required'
        if errors:
            return render(request, 'auth/login_page.html', {"errors": errors})
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "User logged in successfully")
            return redirect('index')
    return render(request, 'auth/login_page.html')
            
            
    
