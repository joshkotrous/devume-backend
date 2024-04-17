from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from devume.models.city import City
from devume.authentication.api_key_authentication import ApiKeyAuthentication
from devume.serializers.city_serializer import CitySerializer

class CitiesListView(ListAPIView):
    authentication_classes = [ApiKeyAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesRetrieveView(RetrieveAPIView):
    authentication_classes = [ApiKeyAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesCreateView(CreateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CitiesUpdateView(UpdateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all()
    serializer_class = CitySerializer
