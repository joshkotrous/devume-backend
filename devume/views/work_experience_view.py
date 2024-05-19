from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.work_experience import WorkExperience
from devume.authentication.bearer_authentication import BearerTokenAuthentication
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

    def get_queryset(self):
        """
        Get the queryset filtered by the profile object.
        """
        # Get the profile object based on the lookup field value
        profile_id = self.kwargs.get(self.lookup_field)
        try:
            profile = Profile.objects.get(uuid=profile_id)
        except Profile.DoesNotExist:
            # Return an empty queryset if the profile does not exist
            return WorkExperience.objects.none()

        # Filter the queryset based on the profile object
        queryset = WorkExperience.objects.filter(profile=profile)

        return queryset


class WorkExperienceUpdateView(UpdateAPIView):
    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class WorkExperienceCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
