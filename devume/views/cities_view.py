from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated
from devume.models.city import City
from devume.authentication.bearer_authentication import BearerTokenAuthentication
from devume.serializers.city_serializer import CitySerializer

class CitiesListView(ListAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesRetrieveView(RetrieveAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesCreateView(CreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesUpdateView(UpdateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
