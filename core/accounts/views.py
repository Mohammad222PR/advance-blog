from django.shortcuts import render, HttpResponse
from time import time
from .tasks import sendEmail
# Create your views here.
def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done bro</h1>")