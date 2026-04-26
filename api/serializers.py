from rest_framework import serializers
from .models import Role, Room, Booking, AccessRoleRule
from django.utils import timezone


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField()
    location = serializers.CharField()
    manager_id = serializers.IntegerField(required=False, allow_null=True)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel_id']


class ReviewSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(allow_null=True)
    hotel_id = serializers.IntegerField()
    booking_id = serializers.IntegerField()
    rating = serializers.CharField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class ReviewReplySerializer(serializers.Serializer):
    manager_id = serializers.IntegerField(allow_null=True)
    review_id = serializers.IntegerField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)


class AccessRoleRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRoleRule
        fields = ['id', 'role_id', 'element_id', 'can_read', 'can_read_all',
                  'can_edit', 'can_edit_all', 'can_create', 'can_delete', 'can_delete_all']
        read_only_fields = ['role_id', 'element_id']


class BookingSerializer(serializers.Serializer):
    room_id = serializers.IntegerField()
    guest_id = serializers.IntegerField()
    check_in_date = serializers.DateTimeField()
    check_out_date = serializers.DateTimeField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError('Wrong check out date')

        if data['check_in_date'] < timezone.now():
            raise serializers.ValidationError('Check out date in past')

        overlapping_bookings = Booking.objects.filter(
            room_id=data['room_id'],
            check_in_date__lt=data['check_out_date'],
            check_out_date__gt=data['check_in_date']
        ).exists()

        if overlapping_bookings:
            raise serializers.ValidationError(
                'The room is already booked for these dates')

        return data
