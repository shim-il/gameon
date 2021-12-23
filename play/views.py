from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def math_instructions_view(request):
    return render(request, "play/math_instructions.html") 

def play_math_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "play/play_math.html")


