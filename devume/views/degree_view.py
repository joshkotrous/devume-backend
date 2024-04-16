from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from devume.models.degree import Degree
from devume.authentication.bearer_authentication import BearerTokenAuthentication


class DegreeListView(APIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Degree.objects.all()
    def get(self, request):
        enum_values = [degree.value for degree in Degree]
        return Response(enum_values)