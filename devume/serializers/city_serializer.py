from rest_framework import serializers
from devume.models.city import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
