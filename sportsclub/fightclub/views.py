from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Membership, UserMembership, Group, SportTest, UserProfile, UserSportResult
from django.contrib.auth.models import User
#siap sau zen of python
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


def prices(request):
    memberships = Membership.objects.all()
    context = {
        'memberships': memberships,
    }
    return render(request, 'fightclub/prices.html', context=context)


@login_required
def profile(request):
    """ideti user membership info, grupou info"""
    # profile = User.objects.all().filter(username=request.user.username)
    # context = {
    #     'profile': profile,
    # }
    return render(request, 'fightclub/profile.html')


@login_required
def user_sport_results(request):
    results = UserSportResult.objects.filter(user=request.user.id).order_by('date')[::-1]
    return render(request, 'fightclub/results.html', {'results': results})
