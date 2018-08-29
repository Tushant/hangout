from django.contrib.auth import authenticate

from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class Login(APIView):

    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = {}
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            data['error'] = "Please provide both username and password"
            return Response(data, status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            data['error'] = "Invalid credentials"
            return Response(data, status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return Response(data, status.HTTP_200_OK)
