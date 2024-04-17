from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)

from rest_framework.permissions import IsAuthenticated
from devume.models.country import Country
from rest_framework.authentication import SessionAuthentication
from devume.authentication.api_key_authentication import ApiKeyAuthentication

from devume.serializers.country_serializer import CountrySerializer


class CountriesListView(ListAPIView):
    authentication_classes = [ApiKeyAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountriesRetrieveView(RetrieveAPIView):
    authentication_classes = [ApiKeyAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountriesCreateView(CreateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountriesUpdateView(UpdateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
