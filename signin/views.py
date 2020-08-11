from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

import string
import random


def login(request):
    if request.method == "POST":
        login_name = request.POST['login_name']
        login_password = request.POST['login_password']

        user = auth.authenticate(username=login_name,password=login_password)

        if user is not None:
            auth.login(request,user)
            return redirect('/home/')
        else:
            return render(request, 'account/login.html')

    else:
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return render(request,'account/welcome.html')


def forgotPassword(request):
    return render(request, 'account/forgotpwd.html')

def email(request):
    tomail = request.POST['user_email']
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
    if request.method == "POST":
            subject = "Email verification"
            message = res
            frommail = "ananthu3454@gmail.com"
            tomail = tomail
            email = EmailMessage(subject, message, frommail, [tomail])
            email.send()
            print("emailsend")

            if User.objects.filter(email=tomail).exists():
                user=User.objects.get(email=tomail)
                user.set_password(str(res))
                user.save()
                print(user.password)
    return render(request, 'account/welcome.html')

def resetPwd(request):
    return render(request, 'account/changePW.html')

def newPassword(request):
    if request.method == "POST":
        user = request.user
        print(user)
        res = request.POST['new_password']
        user.set_password(str(res))
        user.save()
    return render(request, 'account/welcome.html')