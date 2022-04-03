from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from private.models import NewRegister

# Create your views here.
def home(request):
    if request.method == "POST":
        search_vote_no = request.POST['voteridnumber']
        search_name = request.POST['fullname']
        if len(search_vote_no) == 10:
            if NewRegister.objects.filter(voterid=search_vote_no).exists() and NewRegister.objects.filter(fullname=search_name).exists():
                success = "Your Vote has been succesfully registered in Vote Check"
                return render(request, 'public/home.html',{'success':success})
            failure = "Your Vote yet to be registered in Vote Check"
            return render(request, 'public/home.html',{'failure':failure})
        return render(request, 'public/home.html',{'error':"Worng Name or Voter id number"})
    return render(request, 'public/home.html')

def complain(request):
    return render(request, 'public/complain.html')

# def search(request):
    
