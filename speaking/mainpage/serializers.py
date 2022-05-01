from datetime import datetime, timedelta

import pytz
from django.utils import timezone

from django.shortcuts import redirect
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainpage.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'country', 'level', 'connect', 'question']

    def create(self, validated_data):
        user, created = User.objects.update_or_create(
            idd=validated_data.get('idd', None),
            defaults={**validated_data})
        return user


@api_view(['POST'])
def add_user(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        request_data = {}
        request_data.update(request.data.dict() if hasattr(request.data, 'dict') else request.data)
        api_not = request_data.pop('csrfmiddlewaretoken', None)
        request_data['idd'] = request.META.get('REMOTE_ADDR')
        request_data['date'] = timezone.now()
        serializer = UserSerializer(data=request_data)
        if serializer.is_valid():
            serializer.create(request_data)
            if api_not is None:
                user = User.objects.get(idd=request.META.get('REMOTE_ADDR'))
                return Response({'user_id': user.id})
            return redirect(request.META.get('HTTP_REFERER', '/'))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        d = datetime.utcnow().replace(tzinfo=pytz.utc) - timedelta(hours=2)
        users = User.objects.filter(date__gte=d).all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
