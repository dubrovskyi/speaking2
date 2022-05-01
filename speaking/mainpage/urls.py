from django.urls import path

from .views import index
from .serializers import add_user

urlpatterns = [
    path('', index, name='index'),
    path('api/users/add_user', add_user, name='add_user'),
    path('add_user', add_user, name='add_user'),
]
