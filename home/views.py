from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth  import authenticate,  login, logout
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    context = {
        "variable1": "Harry is great",
        "variable2": "Rohan is great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")


def tutorials(request):
    return render(request, 'tutorial.html')


def html(request):
    return render(request, 'htmlTuto.html')


def css(request):
    return render(request, 'css.html')

def blog(request):
    return render(request, 'blog.html')


def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')


def js(request):
    return render(request, 'js.html')

def python(request):
    return render(request, 'python.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def handleSignUp(request):
    if  request.method == "POST":
        username = request.POST['usename']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, "Massage : Username only have 10 character !")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Massage : Username Must Alpha Numeric !")
            return redirect('home')
 
        if pass1 != pass2:
            messages.error(request, "Massage : password dose not match !")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your Account has been successfully created !")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
 
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')