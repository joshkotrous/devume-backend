from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import connection
from devume.authentication.api_key_authentication import ApiKeyAuthentication


class HealthCheckView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Perform health checks here
        database_status = self.check_database()
        if database_status:
            return Response({"status": "ok"})
        else:
            return Response({"status": "error"}, status=500)

    def check_database(self):
        try:
            # Attempt to execute a simple query to check database connectivity
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                row = cursor.fetchone()
                if row:
                    return True
                else:
                    return False
        except Exception:
            # Log the exception or handle it accordingly
            return False
