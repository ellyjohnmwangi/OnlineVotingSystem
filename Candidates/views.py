from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Position, Candidate
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
import matplotlib

matplotlib.use('Agg')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('index')
            else:
                return HttpResponseRedirect("Account disabled")
        else:
            print("Invalid credentials: {0}, {1}".format(username, password))
            return HttpResponseRedirect("Invalid login credentials")
    else:
        return render(request, 'login.html', {})


@login_required(redirect_field_name='login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/Vote/home/')


class IndexView(TemplateView):
    template_name = 'templates/index.html'
    context = {}


def vote(request):
    context = {}
    try:
        pos = Position.objects.all()
        user = User.objects.get(username=request.user.username)
        profile = UserProfile.objects.get(user=user)
        context['candidates'] = []
        if profile.voted:
            return HttpResponseRedirect('/Vote/voted/')
        else:
            for c in pos:
                can = []
                candidate = Candidate.objects.filter(candidate=c)
                for i in range(0, c.no_of_candidates):
                    can.append([candidate[i], c.position])
                context['candidates'].append(can)
    except:
        return HttpResponseRedirect("/Vote/login/")
    if request.method == 'POST':
        pos = Position.objects.all()
        for c in pos:
            s = 'candidate' + c.position
            selected_candidate = Candidate.objects.get(pk=request.POST[s])
            selected_candidate.votes += 1
            selected_candidate.save()
            profile.voted = True
            profile.save()
        else:
            print("No Post")

    return render(request, 'Vote/vote.html', context)

