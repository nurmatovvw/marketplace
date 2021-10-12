from django.shortcuts import render
from django.contrib.auth import login, logout

def signout(request):
    logout(request)

    return render(request, 'index.html')