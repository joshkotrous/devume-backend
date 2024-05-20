from rest_framework import serializers
from devume.models.education import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

    def create(self, validated_data):
        # Remove profile from validated_data if it exists, we'll set it in the view
        user_profile = self.context["request"].user.profile
        validated_data["profile"] = user_profile
        return super().create(validated_data)
