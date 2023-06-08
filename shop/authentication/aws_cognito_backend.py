import os
from jose import jwt
import requests
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AWSCognitoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract the token from the request
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        # Retrieve AWS Cognito settings from environment variables
        region = os.environ.get('AWS_COGNITO_REGION')
        pool_id = os.environ.get('AWS_COGNITO_POOL_ID')
        client_id = os.environ.get('AWS_COGNITO_CLIENT_ID')

        if not region or not pool_id or not client_id:
            raise AuthenticationFailed('AWS Cognito settings are not configured')

        # Verify the token using the AWS Cognito JWKS
        try:
            jwks_url = f'https://cognito-idp.{region}.amazonaws.com/{pool_id}/.well-known/jwks.json'
            response = requests.get(jwks_url)
            response.raise_for_status()
            jwks = response.json()

            header = jwt.get_unverified_header(token)
            key_index = None
            for i in range(len(jwks['keys'])):
                if header['kid'] == jwks['keys'][i]['kid']:
                    key_index = i
                    break

            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwks['keys'][key_index])
            payload = jwt.decode(token, public_key, algorithms=['RS256'], audience=client_id)

            # Return a user object with the token payload as user attributes
            user = payload
            return (user, token)
        except Exception as e:
            raise AuthenticationFailed('Invalid token')

    def authenticate_header(self, request):
        return 'Bearer'
