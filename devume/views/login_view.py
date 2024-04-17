from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from devume.authentication.api_key_authentication import ApiKeyAuthentication

class LoginView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return Response({'message': 'Error occurred: ' +  str(e)}, status=500)