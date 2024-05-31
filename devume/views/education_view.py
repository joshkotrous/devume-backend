from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.education import Education
from devume.models.profile import Profile
from devume.serializers.education_serializer import EducationSerializer
from devume.authentication.api_key_authentication import ApiKeyAuthentication
from devume.authentication.bearer_authentication import BearerTokenAuthentication


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
            return Education.objects.none()

        # Filter the queryset based on the profile object
        queryset = Education.objects.filter(profile=profile)

        return queryset


class EducationUpdateView(UpdateAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDeleteView(DestroyAPIView):
    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
