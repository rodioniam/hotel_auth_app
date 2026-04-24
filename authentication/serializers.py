from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('Passwords do not match!')
        return data
