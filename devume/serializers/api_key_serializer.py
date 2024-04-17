from rest_framework import serializers
from devume.models.api_key import ApiKey


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        exclude = ["user"]
