from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
# импортация ресурсов для дальнейшей работы и т.д.


def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request,'adduser.html',{'form':form})


