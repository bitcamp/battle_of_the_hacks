from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def organizer_index(request):
    return HttpResponse("success")
