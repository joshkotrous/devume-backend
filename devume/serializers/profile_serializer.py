from rest_framework import serializers
from devume.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        # Automatically set the user field based on the request's user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)