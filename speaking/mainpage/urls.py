from django.urls import path

from .views import index
from .serializers import add_user

urlpatterns = [
    path('', index, name='index'),
    path('add_user', add_user, name='add_user'),
]
