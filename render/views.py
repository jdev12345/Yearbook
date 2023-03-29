from django.shortcuts import render
# Create your views here.

def login(request):
    return render(request,'render/login.html')

def home(request):
    context = {
        "announcements": [
        
    {
      "id": "1",
      "body": "We are soon to start taking testimonials.",
      "important":1,
    },
    {
      "id": "2",
      "body": "Our second annoucement",
      "important":0,
    },
    {
      "id": "3",
      "body": "Third annoucement",
      "important":1,
    }],
        }
    return render(request,'render/home.html',context)