from django.shortcuts import render
from django.http import HttpResponse
from .models import Membership, UserMembership, Group

def index(request):
    text = "Labas baigiamasais darbas"
    context = {text, }
    return render(request, 'fightclub/index.html')

# Create your views here.
