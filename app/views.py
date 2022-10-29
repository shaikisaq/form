from django.shortcuts import render
from app.models import *
import imp 
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'display_topic.html',d)
def display_Webpage(request):
    W=Webpage.objects.all()
    d={'webpages':W}
    return render(request,'display_Webpage.html',d)

