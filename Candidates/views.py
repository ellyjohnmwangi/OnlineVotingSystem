from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import UserProfile, Position, Candidate, User
from django.http import HttpResponseRedirect, request
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Candidate
import matplotlib

matplotlib.use('Agg')


# class UserLoginView(View):
#     def post(self, request):
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect('index')
#                 else:
#                     return HttpResponseRedirect("Account disabled")
#             else:
#                 print("Invalid credentials: {0}, {1}".format(username, password))
#                 return HttpResponseRedirect("Invalid login credentials")
#         else:
#             return render(request, 'login.html', {})


class IndexView(TemplateView):
    template_name = 'candidates/index.html'


class CandidatesView(ListView):
    template_name = 'candidates/vote.html'
    model = Candidate
    context_object_name = 'candidates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CandidatesView, self).get_context_data(**kwargs)

    def vote(request):
        context = {}
        try:
            pos = Position.objects.all()
            user = User.objects.get(username=request.user.username)
            profile = UserProfile.objects.get(user=user)
            context['candidates'] = []
            if profile.voted:
                return HttpResponseRedirect('index')
            else:
                for c in pos:
                    can = []
                    candidate = Candidate.objects.filter(candidate=c)
                    for i in range(0, c.no_of_candidates):
                        can.append([candidate[i], c.position])
                    context['candidates'].append(can)
        except:
            return HttpResponseRedirect("index")
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

        return render(request, 'candidate/vote.html', context)


class RegisterView(CreateView):
    template_name = 'candidates/register.html'
    form_class = RegisterForm
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'candidates/login.html'


class UserLogoutView(LogoutView):
    template_name = 'candidates/login.html'


# class VoteView(View):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.method = None
#
#     def vote(self):
#         context = {}
#         try:
#             pos = Position.objects.all()
#             user = User.objects.get(username=self.user.username)
#             profile = UserProfile.objects.get(user=user)
#             context['candidates'] = []
#             if profile.voted:
#                 return HttpResponseRedirect('index')
#             else:
#                 for c in pos:
#                     can = []
#                     candidate = Candidate.objects.filter(candidate=c)
#                     for i in range(0, c.no_of_candidates):
#                         can.append([candidate[i], c.position])
#                     context['candidates'].append(can)
#         except:
#             return HttpResponseRedirect("login/")
#         if self.method == 'POST':
#             pos = Position.objects.all()
#             for c in pos:
#                 s = 'candidate' + c.position
#                 selected_candidate = Candidate.objects.get(pk=self.POST[s])
#                 selected_candidate.votes += 1
#                 selected_candidate.save()
#                 profile.voted = True
#                 profile.save()
#             else:
#                 print("No Post")
#
#         return render(self, 'vote.html', context)