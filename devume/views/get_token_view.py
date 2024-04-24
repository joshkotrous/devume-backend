from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class GenerateTokenView(APIView):
    def post(self, request):
        # Retrieve user credentials from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate the user (this may vary based on your authentication backend)
        user = authenticate(username=username, password=password)

        # Check if the user is authenticated
        if user:
            # Delete existing tokens if any
            Token.objects.filter(user=user).delete()

            # Create a new token for the authenticated user
            token = Token.objects.create(user=user)

            # Return the token in the response
            return Response({"token": token.key, "user_id": user.id})
        else:
            # Return an error response if authentication fails
            return Response({"error": "Invalid credentials"}, status=400)
