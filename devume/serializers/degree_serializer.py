from rest_framework import serializers
from devume.models.degree import Degree


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"
