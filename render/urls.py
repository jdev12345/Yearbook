from django.urls import path, include
from . import views

urlpatterns = [
        path('login/',views.login),
        path('home/',views.home),
        path('myprofile/',views.myprofile),
]