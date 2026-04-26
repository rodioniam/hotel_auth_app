from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Hotel, Room, Booking, Review, ReviewReply
from .utils import unauthorized, forbidden
from .permissions import check_permission


# ------- Hotel
class MockHotelListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Hotel.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        return Response([
            {'id': 1, 'name': 'Grand Hotel', 'location': 'Moscow', 'manager_id': 2},
            {'id': 2, 'name': 'Night Stay', 'location': 'St.Petersburg', 'manager_id': 3},  # noqa
        ])

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Hotel.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        return Response({'message': 'Hotel created'}, status=status.HTTP_201_CREATED)


class MockHotelDetailView(APIView):
    def get(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Hotel.BUSINESS_ELEMENT, 'read'):
            return forbidden()

        return Response([
            {'id': 1, 'name': 'Grand Hotel', 'location': 'Moscow', 'manager_id': 2},
        ])

    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Hotel.BUSINESS_ELEMENT, 'edit'):
            return forbidden()

        return Response({'message': 'Hotel edited'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Hotel.BUSINESS_ELEMENT, 'delete'):
            return forbidden()

        return Response({'message': 'Hotel deleted'}, status=status.HTTP_200_OK)


# ------- Room
class MockRoomListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Room.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        return Response([
            {'id': 1, 'hotel_id': 1},
            {'id': 2, 'hotel_id': 1},
            {'id': 3, 'hotel_id': 1},
            {'id': 4, 'hotel_id': 2},
            {'id': 5, 'hotel_id': 2},
        ])

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Room.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        return Response({'message': 'Room created'}, status=status.HTTP_201_CREATED)


class MockRoomDetailView(APIView):
    def get(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Room.BUSINESS_ELEMENT, 'read'):
            return forbidden()

        return Response([
            {'id': 1, 'hotel_id': 1},
        ])

    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Room.BUSINESS_ELEMENT, 'edit'):
            return forbidden()

        return Response({'message': 'Room edited'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Room.BUSINESS_ELEMENT, 'delete'):
            return forbidden()

        return Response({'message': 'Room deleted'}, status=status.HTTP_200_OK)


# ------- Booking
class MockBookingListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Booking.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        return Response([
            {
                'id': 1,
                'room_id': 1,
                'guest_id': 2,
                'check_in_date': 'some_date',
                'check_out_date': 'some_date',
                'status': 'new',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
            {
                'id': 2,
                'room_id': 3,
                'guest_id': 4,
                'check_in_date': 'some_date',
                'check_out_date': 'some_date',
                'status': 'confirmed',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
            {
                'id': 3,
                'room_id': 5,
                'guest_id': 1,
                'check_in_date': 'some_date',
                'check_out_date': 'some_date',
                'status': 'in_progress',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
        ])

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Booking.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        return Response({'message': 'Booking created'}, status=status.HTTP_201_CREATED)


class MockBookingDetailView(APIView):
    def get(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Booking.BUSINESS_ELEMENT, 'read'):
            return forbidden()

        return Response([
            {
                'id': 3,
                'room_id': 5,
                'guest_id': 1,
                'check_in_date': 'some_date',
                'check_out_date': 'some_date',
                'status': 'in_progress',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            }
        ])

    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Booking.BUSINESS_ELEMENT, 'edit'):
            return forbidden()

        return Response({'message': 'Booking edited'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Booking.BUSINESS_ELEMENT, 'delete'):
            return forbidden()

        return Response({'message': 'Booking deleted'}, status=status.HTTP_200_OK)


# ------- Review
class MockReviewListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Review.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        return Response([
            {
                'id': 1,
                'user_id': 1,
                'hotel_id': 2,
                'booking_id': 2,
                'rating': '5',
                'text': 'review text',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
            {
                'id': 2,
                'user_id': 4,
                'hotel_id': 1,
                'booking_id': 1,
                'rating': '4',
                'text': 'review text',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
            {
                'id': 3,
                'user_id': 2,
                'hotel_id': 2,
                'booking_id': 3,
                'rating': '5',
                'text': 'review text',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            },
        ])

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Review.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        return Response({'message': 'Review created'}, status=status.HTTP_201_CREATED)


class MockReviewDetailView(APIView):
    def get(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Review.BUSINESS_ELEMENT, 'read'):
            return forbidden()

        return Response([
            {
                'id': 1,
                'user_id': 1,
                'hotel_id': 2,
                'booking_id': 2,
                'rating': '5',
                'text': 'review text',
                'created_at': 'some_date',
                'updated_at': 'some_date'
            }
        ])

    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Review.BUSINESS_ELEMENT, 'edit'):
            return forbidden()

        return Response({'message': 'Review edited'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, Review.BUSINESS_ELEMENT, 'delete'):
            return forbidden()

        return Response({'message': 'Review deleted'}, status=status.HTTP_200_OK)


# ------- ReviewReply
class MockReviewReplyListView(APIView):
    def get(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, ReviewReply.BUSINESS_ELEMENT, 'read_all'):
            return forbidden()

        return Response([
            {
                'id': 1,
                'manager_id': 1,
                'review_id': 1,
                'text': 'review text',
                'created_at': 'some_date'
            },
            {
                'id': 2,
                'manager_id': 2,
                'review_id': 2,
                'text': 'review text',
                'created_at': 'some_date'
            },
            {
                'id': 3,
                'manager_id': 1,
                'review_id': 3,
                'text': 'review text',
                'created_at': 'some_date'
            },
        ])

    def post(self, request):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, ReviewReply.BUSINESS_ELEMENT, 'create'):
            return forbidden()

        return Response({'message': 'Review reply created'}, status=status.HTTP_201_CREATED)


class MockReviewReplyDetailView(APIView):
    def get(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, ReviewReply.BUSINESS_ELEMENT, 'read'):
            return forbidden()

        return Response([
            {
                'id': 1,
                'manager_id': 1,
                'review_id': 1,
                'text': 'review text',
                'created_at': 'some_date'
            }
        ])

    def patch(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, ReviewReply.BUSINESS_ELEMENT, 'edit'):
            return forbidden()

        return Response({'message': 'Review reply edited'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.auth_user is None:
            return unauthorized()
        if not check_permission(request.auth_user, ReviewReply.BUSINESS_ELEMENT, 'delete'):
            return forbidden()

        return Response({'message': 'Review reply deleted'}, status=status.HTTP_200_OK)
