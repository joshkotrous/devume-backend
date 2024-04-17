from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.work_experience import WorkExperience
from devume.models.profile import Profile
from devume.serializers.work_experience_serializer import (
    WorkExperienceSerializer,
)
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class WorkExperienceListView(ListAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class WorkExperienceRetrieveView(ListAPIView):
    lookup_field = "profile_id"  # Set the lookup field to 'profile_id'

    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class WorkExperienceUpdateView(UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class WorkExperienceCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        user_profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=user_profile)
