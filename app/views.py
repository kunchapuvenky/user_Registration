from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
from django.core.mail import send_mail

# Create your views here.


def Registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'UFO':UFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()


            send_mail('Registration',
                      'Registration successfully done',
                      'kunchapuvenkateswarlu8@gmail.com',
                      [NSUO.save],
                      fail_silently=True)


            return HttpResponse('Registration is successful')
        else:
            return HttpResponse('Not valid')


    return render(request,'Registration.html',d)