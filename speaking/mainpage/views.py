import pytz
from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from .forms import UserForm
from .models import User
from .serializers import UserSerializer


class HomeUser(ListView, CreateView):
    model = User
    template_name = 'mainpage/index.html'


def index(request):
    d = datetime.utcnow().replace(tzinfo=pytz.utc) - timedelta(hours=2)
    users = User.objects.filter(date__gte=d).all()
    context = {
        'users': users,
        'form': UserForm(),
    }
    return render(request, 'mainpage/index.html', context)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

