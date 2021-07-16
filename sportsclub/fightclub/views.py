from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Membership, UserMembership, Group
import this

def index(request):
    text = "Labas baigiamasais darbas"
    context = {
        'text': text,
    }
    return render(request, 'fightclub/index.html', context=context)

def about(request):
    return render(request, 'fightclub/about.html')

def groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'fightclub/groups.html', context=context)

def group(request, group_id):
    single_group = get_object_or_404(Group, pk=group_id)
    return render(request, 'fightclub/group.html', {'group': single_group})


