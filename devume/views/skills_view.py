from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
    ListAPIView,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from devume.models.skill import Skill
from devume.serializers.skill_serializer import SkillSerializer
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class SkillListView(ListAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillRetrieveView(RetrieveAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillCreateView(CreateAPIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillUpdateView(UpdateAPIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
