from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import UserProfile, Position, Candidate, User
from django.http import HttpResponseRedirect, request
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Candidate, Position
import matplotlib

matplotlib.use('Agg')


class IndexView(TemplateView):
    template_name = 'candidates/index.html'


class CandidatesView(ListView):
    template_name = 'candidates/vote.html'
    model = Candidate
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CandidatesView, self).get_context_data(**kwargs)
        return context

    # def vote(self):
    #     p = get_object_or_404(Candidate, )
    #     try:
    #         pos = Position.objects.all()
    #         user = User.objects.get(username=self.user.username)
    #         profile = UserProfile.objects.get(user=user)
    #         context['candidates'] = []
    #         if profile.voted:
    #             return HttpResponseRedirect('index')
    #         else:
    #             for c in pos:
    #                 can = []
    #                 candidate = Candidate.objects.filter(candidate=c)
    #                 for i in range(0, c.no_of_candidates):
    #                     can.append([candidate[i], c.position])
    #                 context['candidates'].append(can)
    #     except:
    #         return HttpResponseRedirect("index")
    #     if self.method == 'POST':
    #         pos = Position.objects.all()
    #         for c in pos:
    #             s = 'candidate' + c.position
    #             selected_candidate = Candidate.objects.get(pk=self.POST[s])
    #             selected_candidate.votes += 1
    #             selected_candidate.save()
    #             profile.voted = True
    #             profile.save()
    #         else:
    #             print("No Post")
    #
    #     return render(self, 'candidate/vote.html', context)


class VotingView(ListView):
    template_name = 'candidates/voting.html'
    model = Candidate
    context_object_name = 'candidates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VotingView, self).get_context_data(**kwargs)
        return context


class ResultsViews(ListView):
    template_name = 'candidates/results.html'
    model = Candidate
    context_object_name = "votes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ResultsViews, self).get_context_data(**kwargs)
        return context


class PositionDetail(ListView):
    model = Candidate
    template_name = 'candidates/positions.html'
    context_object_name = 'candidates'

    def get_queryset(self):
        self.post = get_object_or_404(Position, slug=self.kwargs['slug'])
        return Candidate.objects.filter(post=self.post).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(PositionDetail, self).get_context_data(**kwargs)
        self.post = get_object_or_404(Position, slug=self.kwargs['slug'])
        context['post'] = self.post
        return context


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
