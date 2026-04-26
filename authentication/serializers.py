"""
Аналог формы в обычном Django
"""


from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(required=False)
    last_name = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords do not match!')
        return data


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name']
        extra_kwargs = {
            'middle_name': {'required': False, 'allow_null': True}
        }


class UserProfileAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'is_active', 'created_at']  # noqa
        extra_kwargs = {
            'middle_name': {'required': False, 'allow_null': True}
        }


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    new_password_confirm = serializers.CharField()

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError('Passwords do not match!')
        return data
