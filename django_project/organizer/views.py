from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from organizer.forms import UploadFileFormView
from organizer.models import Attendee

from login.models import Registrant

import os
import csv

# Create your views here.
def organizer_index(request):
    if(request.method == 'POST'):
        form = UploadFileFormView(request.POST, request.FILES)
        if (form.is_valid()):
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/organizer/upload/')
    else:
        form = UploadFileFormView()
    return render_to_response(
        'form.html', 
        {
            'form': form,
            'url': '/organizer/'
        },
	context_instance=RequestContext(request),
    )

def handle_uploaded_file(f):
    with open('fi_up.csv', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)

    with open('fi_up.csv', 'r+') as fi: 
        for line in fi:
            attributes = line.split(',')
            try:
                if(count(Attendee.objects.filter(email = attributes[2])) > 0 ):
                    continue
                a = Attendee(
                    first_name = attributes[0],
                    last_name = attributes[1],
                    email = attributes[2],
                    school = attributes[3],
                    image = attributes[4],
                )
                a.save()
            except:
                print line

    os.system("rm fi_up.csv")

def organizer_upload(request):
    return render_to_response(
        "success.html",
        {},
        context_instance=RequestContext(request),
    )

def write_obj(writer, entity):
    writer.writerow([entity.first_name, entity.last_name, entity.email, entity.school])

def get_checkins(request):
    response = HttpResponse(content_type='text/csv')    
    response['Content-Disposition'] = 'attachment; filename="checkins.csv"'
    writer = csv.writer(response)
    for checkin in Registrant.objects.all():
        write_obj(writer, checkin)
    return response

def get_prereg(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="preregs.csv"'
    writer = csv.writer(response)
    for prereg in Attendee.objects.all():
        write_obj(writer, prereg)
    return response
