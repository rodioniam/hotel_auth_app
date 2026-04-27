"""
Аналог формы в обычном Django
"""


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all(),
                            message='Account with such email already exists!')
        ]
    )
    password = serializers.CharField()
    password_confirm = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Password must contain at least 10 characters')  # noqa
        return value

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
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'role_id', 'is_active', 'created_at']  # noqa
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

    def validate_new_password(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Password must contain at least 10 characters')  # noqa
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError('Passwords do not match!')
        return data
