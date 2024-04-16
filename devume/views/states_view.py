from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated
from devume.models.state import State

from devume.authentication.bearer_authentication import BearerTokenAuthentication
from devume.serializers.state_serializer import StateSerializer

class StatesListView(ListAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StatesRetrieveView(RetrieveAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StatesCreateView(CreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StatesUpdateView(UpdateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all()
    serializer_class = StateSerializer
