from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.education import Education
from devume.models.profile import Profile
from devume.serializers.education_serializer import EducationSerializer
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class EducationListView(ListAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationRetrieveView(ListAPIView):
    lookup_field = "profile_id"
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationUpdateView(UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        user_profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=user_profile)
