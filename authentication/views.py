from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, BlackListedToken
from .utils import hash_password, check_password, generate_token, decode_token
from .serializers import *


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            User.objects.create(
                email=validated_data['email'],
                password_hash=hash_password(validated_data['password']),
                first_name=validated_data['first_name'],
                middle_name=validated_data.get('middle_name'),
                last_name=validated_data['last_name']
            )
            return Response({'message': 'User registered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            try:
                user = User.objects.get(email=validated_data['email'])
                if not user.is_active:
                    return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({'error': 'Wrong email or password'}, status=status.HTTP_401_UNAUTHORIZED)
            if check_password(validated_data['password'], user.password_hash):
                token = generate_token(user.pk)
                return Response({'Token': token})
            return Response({'error': 'Wrong email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        # тут не нужно делать валидацию так как читаю базу данных
        # так же не надо передавать request через data=, так как просто читаю базу
        serializer = UserProfileSerializer(request.auth_user)
        return Response(serializer.data)


class ProfileUpdateView(APIView):
    def patch(self, request):

        if request.auth_user is None:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        update_serializer = UserUpdateSerializer(data=request.data)

        if update_serializer.is_valid():
            update_data = update_serializer.validated_data
            for k, v in update_data.items():
                setattr(request.auth_user, k, v)
            request.auth_user.save()

            serializer = UserProfileSerializer(request.auth_user)
            return Response(serializer.data)
        return Response(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        if request.auth_user is None:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        token = request.headers.get('Authorization').split(' ')[1]
        BlackListedToken.objects.create(
            token=token
        )

        return Response({'message': 'You are logged out'}, status=status.HTTP_200_OK)


class PasswordChangeView(APIView):
    def patch(self, request):

        if request.auth_user is None:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PasswordChangeSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data

            if check_password(validated_data['old_password'], request.auth_user.password_hash):
                request.auth_user.password_hash = hash_password(
                    validated_data['new_password'])
                request.auth_user.save()
                return Response({'message': 'Password changed'}, status=status.HTTP_200_OK)
            return Response({'error': 'Wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDeleteView(APIView):
    def delete(self, request):
        if request.auth_user is None:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        request.auth_user.is_active = False
        request.auth_user.save()
        return Response({'message': 'Account deleted'})
