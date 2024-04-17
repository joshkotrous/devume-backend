from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from devume.authentication.api_key_authentication import ApiKeyAuthentication
class NotFound(APIView):
    authentication_classes = [SessionAuthentication, ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]
    # queryset = Degree.objects.all()
    def get(self, request):
        return Response({
            'status_code': 404,
            'error': 'The resource was not found'
        }, 404)
    
    def post(self, request):
        return Response({
            'status_code': 404,
            'error': 'The resource was not found'
        }, 404)
    
    def put(self, request):
        return Response({
            'status_code': 404,
            'error': 'The resource was not found'
        }, 404)
    
    def patch(self, request):
        return Response({
            'status_code': 404,
            'error': 'The resource was not found'
        }, 404)
    