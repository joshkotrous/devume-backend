from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from devume.models.degree import Degree
from rest_framework.authentication import SessionAuthentication
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class DegreeListView(APIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        enum_values = [degree.value for degree in Degree]
        return Response(enum_values)