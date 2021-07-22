from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Membership, UserMembership, Group, SportTest, UserProfile, UserSportResult
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
# siap sau zen of python
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


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username,first_name=first_name, last_name=last_name,
                                             email=email, password=password)
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')
