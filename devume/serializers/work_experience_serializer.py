from rest_framework import serializers
from devume.models.work_experience import WorkExperience
from devume.models.profile import Profile


class WorkExperienceSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), required=False)

    class Meta:
        model = WorkExperience
        fields = "__all__"

    def create(self, validated_data):
        # Remove profile from validated_data if it exists, we'll set it in the view
        user_profile = self.context["request"].user.profile
        validated_data["profile"] = user_profile
        return super().create(validated_data)
