from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
from rest_framework.permissions import AllowAny


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Perform health checks here
        if True:
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
