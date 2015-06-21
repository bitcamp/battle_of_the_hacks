from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from login.forms import EmailFormView
from login.models import Registrant

from organizer.models import Attendee

import os

Allowed_ips = []

def waiver_page(request, fname, email):
    return render_to_response(
        'waiver.html',
        {
            'first_name': fname,
            'email': email
        },
        context_instance = RequestContext(request)
    )

def verifyWaiver(request):
    att = Attendee.objects.filter(email = request.POST['email'])[0]
    reg = Registrant(
        first_name = att.first_name,
        last_name = att.last_name,
        email = att.email,
        school = att.school,
        image = att.image,
    )
    reg.save()
    Allowed_ips.append(get_client_ip(request))
    return render_to_response(
        'welcome.html',
        {
            'first_name': att.first_name,
            'last_name': att.last_name,
            'email': att.email,
            'school': att.school,
            'image': att.image,
        },
        context_instance = RequestContext(request)
    )

import dns.resolver

res = dns.resolver.Resolver()
res.nameservers = ['8.8.8.8']

def DNSlookup(URL):
    home = URL.split('//')[-1].split('/')[0]
    record = res.query(home).response.answer[0].to_text()
    ip = ''
    for c in record[::-1]:
     if c in '0123456789.':
         ip += c
     else:
         break
    ip = ip[::-1]
    return URL.replace(home, ip)

# Create your views here.
def login_index(request):
    		
    if(request.method == "POST"):
        form = EmailFormView(request.POST)
        if(form.is_valid()):
            matches = Attendee.objects.filter(email = request.POST['email'])
            if(matches.count() > 0):
                att = matches[0]
                if(Registrant.objects.filter(email = att.email).count() == 0):
                    return waiver_page(request, att.first_name, att.email)                
                Allowed_ips.append(get_client_ip(request))
                return render_to_response(
                    'welcome.html',
                    {
                        'first_name': att.first_name,
                        'last_name': att.last_name,
                        'email': att.email,
                        'school': att.school,
                        'image': att.image,
                    },
                    context_instance = RequestContext(request)
                )
            else:
                return HttpResponseRedirect('/denied/')
    else:
        form = EmailFormView(auto_id = False)
    return render_to_response(
        'login.html',
        {
            'form': form
        },
        context_instance = RequestContext(request)
    )

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def denied(request):
    return render_to_response(
        'sorry.html',
        {},
        context_instance = RequestContext(request)
    )
