from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.profile import Profile
from devume.serializers.profile_serializer import ProfileSerializer
from devume.serializers.user_serializer import UserSerializer

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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = []
        for profile in serializer.data:
            profile_instance = Profile.objects.get(pk=profile["uuid"])
            user_instance = profile_instance.user
            profile["user"] = {
                "id": user_instance.id,
                "username": user_instance.username,
                "first_name": user_instance.first_name,
                "last_name": user_instance.last_name,
                "email": user_instance.email,
                # Add more user-related data as needed
            }

            data.append(profile)
        return Response(data)


class ProfileRetrieveView(RetrieveAPIView):
    authentication_classes = [
        SessionAuthentication,
        ApiKeyAuthentication,
        BearerTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_context(self):
        profile = super().get_object()

        context = super().get_serializer_context()
        context["user"] = profile.user
        return context

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        profile_serializer = self.get_serializer(instance)
        user_serializer = UserSerializer(instance.user)
        return Response({"profile": profile_serializer.data, "user": user_serializer.data})


class ProfileRetrieveByUserIDView(RetrieveAPIView):
    authentication_classes = [
        SessionAuthentication,
        ApiKeyAuthentication,
        BearerTokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get("user_id")
        try:
            profile = Profile.objects.get(user_id=user_id)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=404)


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
