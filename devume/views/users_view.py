from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, UpdateAPIView ,CreateAPIView, ListAPIView
from devume.serializers.user_serializer import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer