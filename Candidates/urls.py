from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLoginView.as_view(), name="logout"),
    path('register/', UserLoginView.as_view(), name="register"),
    ]
