from rest_framework.generics import CreateAPIView

from devume.permissions.is_super_user_permission import IsSuperuserPermission
from devume.models.api_key import ApiKey
from devume.serializers.api_key_serializer import ApiKeySerializer
from devume.authentication.bearer_authentication import (
    BearerTokenAuthentication,
)


class ApiKeyCreateView(CreateAPIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsSuperuserPermission]
    queryset = ApiKey.objects.all()
    serializer_class = ApiKeySerializer

    def perform_create(self, serializer):
        # Set the user_id field to the ID of the authenticated user
        serializer.save(user=self.request.user)
