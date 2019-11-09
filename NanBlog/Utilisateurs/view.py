from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import Group
from . import models
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.conf import settings
from django.http import JsonResponse
import json


def inscription(request):
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            group=form.cleaned_data.get("groups")
            print(group[0], email)
            user = form.save()
            user.is_active = False
            user.save()
            users = models.MyUser.objects.filter(email=email)
            choice=group[0]
            groupe = Group.objects.get( name = choice )
            for item in users:
                print(item.id)
                item.groups.add(groupe)
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            # mail = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            url= 'http://mysiteapi.tk/html'
    
            data = {
                    'subject': mail_subject,
                    'message': message,
                    'to': to_email ,
                    'key': ")H@MbQeThWmZq4t7w!z%C*F-JaNdRgUj" ,
                }
            req = requests.post(url, data=data)
            return redirect('sign_send_verif')
    else:
        form= forms.RegistrationForm()
    return render(request, 'account/signup.html', {
        'form':form
    })

def signup_sendmail(request):
    return render(request, 'account/signup_confirm.html')
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
    #         # email.send()
    #         return HttpResponse('Please confirm your email address to complete the registration')
    # else:
    #     form = SignupForm()
    # return render(request, 'signup.html', {'form': form})
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = models.MyUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, models.MyUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
    else:
        return render(request, 'account/invalid_link.html')
    
def sendregister(request):
    try:
        postdata = json.loads(request.body.decode('utf-8'))
        name = postdata['name']
        email = postdata['email']    
        password = postdata['password']
        repass = postdata['repass']
        visiteur = postdata['visiteur']
        membre = postdata['membre']
        
        print(name,email,password,repass,visiteur,membre)
        isSucces = False
        cont = 1
        
        # if name is not None and password is not None and repass is not None and email is not None:
        #     isSucces = True
        #     h = MyUser(first_name=name,email=email,password=password,repass=repass,groups=visiteur)
        #     h.save()
        #     print(nom,user,contact,email,password,repass)
        # else:
        #     isSucces = False

        # while cont < 100000000:
        #     cont += 1
    except:
        print("error")

    datas = {
        'succes': True,
        # 'nom': nom,
        # 'cont': cont
    }
    return JsonResponse(datas, safe=False)