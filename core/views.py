from django.shortcuts import render
from .models import *
def home(request):
    post = Company.objects.all()
    return render(request,'index.html',{'post':post})
