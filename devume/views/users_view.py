from django.contrib.auth.models import User
from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from devume.serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from devume.authentication.bearer_authentication import BearerTokenAuthentication

from devume.permissions.is_super_user_permission import IsSuperuserPermission
from devume.authentication.api_key_authentication import ApiKeyAuthentication

class UserListView(ListAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsSuperuserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
