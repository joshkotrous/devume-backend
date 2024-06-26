from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)

from rest_framework.permissions import IsAuthenticated
from devume.models.state import State
from rest_framework.authentication import SessionAuthentication
from devume.serializers.state_serializer import StateSerializer
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class StatesListView(ListAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StatesRetrieveView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StatesCreateView(CreateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StatesUpdateView(UpdateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer
