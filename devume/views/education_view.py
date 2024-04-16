from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.education import Education
from devume.models.profile import Profile
from devume.serializers.education_serializer import EducationSerializer
from devume.authentication.bearer_authentication import BearerTokenAuthentication


class EducationListView(ListAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
class EducationRetrieveView(ListAPIView):
    lookup_field = 'profile_id'  # Set the lookup field to 'profile_id'

    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationUpdateView(UpdateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationCreateView(CreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        user_profile = Profile.objects.get(user=self.request.user)
        serializer.save(profile=user_profile)
