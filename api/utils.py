from rest_framework import status
from rest_framework.response import Response


def unauthorized():
    return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


def forbidden():
    return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
