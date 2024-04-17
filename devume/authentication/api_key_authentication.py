from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from devume.models.api_key import ApiKey


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-Api-Key")

        if not api_key:
            return None

        try:
            api_key_obj = ApiKey.objects.get(key=api_key)
        except ApiKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")

        return (api_key_obj.user, api_key_obj)
