from django.shortcuts import render
# Create your views here.

def login(request):
    render(request,'home/login.html')