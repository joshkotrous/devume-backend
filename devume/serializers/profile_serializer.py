from rest_framework import serializers
from devume.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude=['user']

        