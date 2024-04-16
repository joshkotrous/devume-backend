from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from devume.authentication.bearer_authentication import BearerTokenAuthentication

class LoginView(APIView):
    authentication_classes = [BearerTokenAuthentication]

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
                token, created = Token.objects.get_or_create(user=user)

                return Response({'session_id': request.session.session_key, 'token': token.key})
            else:
                return Response({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return Response({'message': 'Error occurred: ' +  str(e)}, status=500)