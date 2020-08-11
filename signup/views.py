from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# from .forms import UserSignupForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":

            name = request.POST['user_name']
            email = request.POST['user_email']
            password = request.POST['user_password']
            confirm_password = request.POST['user_confirm_password']

            if password == confirm_password:
                if User.objects.filter(username=name).exists():
                    print ('username taken')
                elif User.objects.filter(email=email).exists():
                    print ('email taken')
                else:
                    user = User.objects.create_user(username=name,email=email,password=password)
                    user.save()
                    return redirect('/accountSignin/')
    else:

        return render(request, 'account/signup.html')
