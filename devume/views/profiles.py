from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView, UpdateAPIView ,CreateAPIView
from devume.models.profile import Profile
from devume.serializers.profile_serializer import ProfileSerializer

class ProfileRetrieveView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreateView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def Profiles(request):
    data = {"message" : "hello world"}
    return JsonResponse(data)