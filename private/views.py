from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from . forms import NewRegisterForm
from . models import NewRegister
import re
# Create your views here.

def loginuser(request):
    if request.method == "GET":
        return render(request, 'private/loginuser.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'] )
        if user is None:
            return render(request, 'private/loginuser.html',{'error':'Wrong Username or Password'})
        else:
            login(request, user)
            return redirect('dashboard')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')

@login_required
def dashboard(request):
    return render(request, 'private/dashboard.html')

@login_required
def new_register(request):
    if request.method == "GET":
        return render(request, 'private/new_register.html',{'NewRegisterForm':NewRegisterForm()})

    else:
        if is_valid_voter_id(request.POST['voterid']) :
            if request.POST['voterid'] == request.POST['cvoterid']:
                try:
                    form = NewRegisterForm(request.POST)
                    newform = form.save(commit=False)
                    newform.user = request.user
                    newform.save()
                    return redirect('dashboard')

                except ValueError:
                    return render(request, 'private/new_register.html',{'NewRegisterForm':NewRegisterForm()})
            else :
                return render(request, 'private/new_register.html',{'NewRegisterForm':NewRegisterForm(),'error':'Voter id and Confirm Voter id did not match.'})
        return render(request, 'private/new_register.html',{'NewRegisterForm':NewRegisterForm(),'error':'Invalid Voter id numver.'})

@login_required
def edit_registers(request):
    registers = NewRegister.objects.filter(user=request.user).order_by('-created')
    return render(request, 'private/edit_registers.html',{'registers':registers})

@login_required
def edit_register_detail(request, register_pk):
    register = get_object_or_404(NewRegister, pk=register_pk, user=request.user)
    return render(request, 'private/edit_register_detail.html',{'register':register})

@login_required
def view_registers(request):
    registers = NewRegister.objects.filter(user=request.user).order_by('-created')
    return render(request, 'private/view_registers.html',{'registers':registers})

@login_required
def help(request):
    return render(request, 'private/help.html')

@login_required
def inbox(request):
    return render(request, 'private/inbox.html')

def is_valid_voter_id(voter_id_no):
    regex = "^([a-zA-Z]){3}([0-9]){7}?$"
    p = re.compile(regex)
    if(re.search(p, voter_id_no) and
       len(voter_id_no) == 10):
        return True
    else:
        return False
