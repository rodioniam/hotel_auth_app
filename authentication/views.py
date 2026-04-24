from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .utils import hash_password
from .serializers import UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            User.objects.create(
                email=validated_data['email'],
                password_hash=hash_password(validated_data['password']),
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            return Response({'message': 'User registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
