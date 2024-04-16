from rest_framework import serializers
from devume.models.education import Education

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['profile']        