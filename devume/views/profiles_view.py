from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.profile import Profile
from devume.serializers.profile_serializer import ProfileSerializer
from devume.authentication.api_key_authentication import ApiKeyAuthentication
from devume.authentication.bearer_authentication import BearerTokenAuthentication


class ProfileListView(ListAPIView):
    authentication_classes = [
        SessionAuthentication,
        ApiKeyAuthentication,
        BearerTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveView(RetrieveAPIView):
    authentication_classes = [
        SessionAuthentication,
        ApiKeyAuthentication,
        BearerTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        # Get the profile object using the default queryset
        profile = super().get_object()

        # Get the user associated with the profile
        user = (
            profile.user
        )  # Assuming the user field in Profile model is a ForeignKey to the User model

        # Combine profile and user data as needed
        combined_data = {
            "profile": ProfileSerializer(profile).data,
            "user": {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name
                # Add more user fields as needed
            },
        }

        return combined_data


class ProfileUpdateView(UpdateAPIView):
    authentication_classes = [SessionAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreateView(CreateAPIView):
    authentication_classes = [ApiKeyAuthentication, BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        serializer.save(user=self.request.user)
