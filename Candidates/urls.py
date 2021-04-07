from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('vote/', CandidatesView.as_view(), name="vote"),
    path('voting/', VotingView.as_view(), name="voting"),
    path('results/', ResultsViews.as_view(), name="results"),
    ]
