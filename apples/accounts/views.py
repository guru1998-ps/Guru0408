from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user =User.objects.create_user(username=username,password=password1,email=email )
        user.save();
        print("user created")
        return redirect('/')
        
    else:

        return render(request,'register.html')
    
