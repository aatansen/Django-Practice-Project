from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def signup(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('signin')
    else:
        form=CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request,'signup.html',context)

def signin(request):
    if request.method=="POST":
        form=Auth_form(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=Auth_form()
    context={
        'form':form
    }
    return render(request,'signin.html',context)

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile_management(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_management')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'profile_management.html', {'form': form})

def add_cash(request):
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid():
            add_cash = form.save(commit=False)
            add_cash.user = request.user
            add_cash.save()
            return redirect('dashboard')
    else:
        form = AddCashForm()
    return render(request, 'transaction_form.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'transaction_form.html', {'form': form})
