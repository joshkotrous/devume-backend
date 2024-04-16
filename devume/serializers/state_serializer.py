from rest_framework import serializers
from devume.models.state import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

        