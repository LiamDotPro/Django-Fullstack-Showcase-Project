from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from ..authentication.aws_cognito_backend import AWSCognitoAuthentication


class TodoListApiView(APIView):
    authentication_classes = [AWSCognitoAuthentication]

    def get(self, request):
        user = request.user
        # Access the authenticated user's attributes from the token payload
        username = user.get('username')
        email = user.get('email')
        # Perform your desired logic using the user attributes
        ...

        return Response({'message': 'Authenticated'})
