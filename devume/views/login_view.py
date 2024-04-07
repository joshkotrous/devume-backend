from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)

                # Generate token
                # token, created = Token.objects.get_or_create(user=user)

                return Response({'session_id': request.session.session_key})
            else:
                return Response({'message': 'Invalid credentials'}, status=400)
        except Exception as e:
            return Response({'message': 'Error occurred: ' +  str(e)})