from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from login.forms import EmailFormView

from organizer.models import Attendee

# Create your views here.
def login_index(request):
    if(request.method == "POST"):
        form = EmailFormView(request.POST)
        if(form.is_valid()):
            matches = Attendee.objects.filter(email = request.POST['email'])
            if(matches.count() > 0):
                att = matches[0]
                return render_to_response(
                    'welcome.html',
                    {
                        'first_name': att.first_name,
                        'last_name': att.last_name,
                        'email': att.email,
                        'school': att.school,
                        'image': att.image
                    },
                    context_instance = RequestContext(request)
                )
            else:
                return HttpResponseRedirect('/denied/')
    else:
        form = EmailFormView()
    return render_to_response(
        'login.html',
        {
            'form': form
        },
        context_instance = RequestContext(request)
    )

def denied(request):
    return HttpResponse("""Email Checked""")
