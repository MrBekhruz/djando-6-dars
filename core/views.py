from django.shortcuts import render,redirect
from .models import *
from .forms import *
def home(request):
    post = Company.objects.all()
    return render(request,'index.html',{'post':post})
def add(request):
    form = CompanyForms(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render('home')

    else:
        form = CompanyForms()
    return render(request,'add.html',{'form':form})