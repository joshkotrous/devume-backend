from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.models.work_experience import WorkExperience
from devume.serializers.work_experience_serializer import WorkExperienceSerializer
from devume.authentication.bearer_authentication import BearerTokenAuthentication


class WorkExperienceListView(ListAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    
class WorkExperienceRetrieveView(RetrieveAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class WorkExperienceUpdateView(UpdateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class WorkExperienceCreateView(CreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        serializer.save(profile=self.request.profile)
