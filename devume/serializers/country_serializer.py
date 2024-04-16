from rest_framework import serializers
from devume.models.country import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

        