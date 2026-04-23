from django.db import models
from django.utils import timezone


class BusinessElement(models.Model):
    element_name = {
        'user': 'User',
        'role': 'Role',
        'hotel': 'Hotel',
        'room': 'Room',
        'review': 'Review',
        'reviewReply': 'Reply',
        'booking': 'Booking',
        'accessRoleRules': 'Access Role Rules'
    }

    name = models.CharField(choices=element_name, unique=True)

    description = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    BUSINESS_ELEMENT = 'role'

    role_names = {
        'guest': 'Guest',
        'hotel_manager': 'Hotel manager',
        'admin': 'Admin'
    }
    name = models.CharField(choices=role_names, unique=True)
    description = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    BUSINESS_ELEMENT = 'hotel'
    # element_id = models.ForeignKey(BusinessElement, on_delete=models.PROTECT)
    name = models.CharField()
    location = models.CharField()
    manager_id = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        db_column='manager_id'
    )

    def __str__(self):
        return self.name


class Room(models.Model):
    BUSINESS_ELEMENT = 'room'
    # element_id = models.ForeignKey(BusinessElement, on_delete=models.PROTECT)
    hotel_id = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        db_column='hotel_id'
    )


class Booking(models.Model):
    STATUS_NEW = 'new'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_FINISHED = 'finished'
    STATUS_CANCELLED = 'cancelled'

    status_list = {
        STATUS_NEW: 'New',
        STATUS_CONFIRMED: 'Confirmed',
        STATUS_IN_PROGRESS: 'In progress',
        STATUS_FINISHED: 'Finished',
        STATUS_CANCELLED: 'Cancelled'
    }

    BUSINESS_ELEMENT = 'booking'
    # element_id = models.ForeignKey(BusinessElement, on_delete=models.PROTECT)
    room_id = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        null=True,
        db_column='room_id'
    )
    guest_id = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        db_column='guest_id'
    )
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    status = models.CharField(choices=status_list, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    ONE_STAR = '1'
    TWO_STARS = '2'
    THREE_STARS = '3'
    FOUR_STARS = '4'
    FIVE_STARS = '5'

    rating_list = {
        ONE_STAR: '1/5',
        TWO_STARS: '2/5',
        THREE_STARS: '3/5',
        FOUR_STARS: '4/5',
        FIVE_STARS: '5/5'
    }

    BUSINESS_ELEMENT = 'review'
    # element_id = models.ForeignKey(BusinessElement, on_delete=models.PROTECT)
    user_id = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='user_id'
    )
    hotel_id = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, db_column='hotel_id')
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE, db_column='booking_id')
    rating = models.CharField(choices=rating_list)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReviewReply(models.Model):
    BUSINESS_ELEMENT = 'reviewReply'
    # element_id = models.ForeignKey(BusinessElement, on_delete=models.PROTECT)
    manager_id = models.ForeignKey(
        'authentication.User',
        on_delete=models.SET_NULL,
        null=True,
        # used this so i can type Review.reply
        related_name='reply',
        db_column='manager_id'
    )
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        db_column='review_id'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AccessRoleRule(models.Model):
    BUSINESS_ELEMENT = 'accessRoleRules'

    element_id = models.ForeignKey(
        BusinessElement,
        on_delete=models.PROTECT,
        db_column='element_id'
    )
    role_id = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        db_column='role_id'
    )

    can_read = models.BooleanField(default=False)
    can_read_all = models.BooleanField(default=False)

    can_edit = models.BooleanField(default=False)
    can_edit_all = models.BooleanField(default=False)

    can_create = models.BooleanField(default=False)

    can_delete = models.BooleanField(default=False)
    can_delete_all = models.BooleanField(default=False)
