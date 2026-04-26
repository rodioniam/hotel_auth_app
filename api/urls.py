from django.urls import path
from .views import *
from .mock_views import *

urlpatterns = [
    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>/', RoleDetailView.as_view()),
    path('access-rules/', AccessRoleListView.as_view()),
    path('access-rules/<int:pk>/', AccessRoleDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),

    # mock-views
    path('mock/hotels/', MockHotelListView.as_view()),
    path('mock/hotels/<int:pk>/', MockHotelDetailView.as_view()),
    path('mock/rooms/', MockRoomListView.as_view()),
    path('mock/rooms/<int:pk>/', MockRoomDetailView.as_view()),
    path('mock/bookings/', MockBookingListView.as_view()),
    path('mock/bookings/<int:pk>/', MockBookingDetailView.as_view()),
    path('mock/reviews/', MockReviewListView.as_view()),
    path('mock/reviews/<int:pk>/', MockReviewDetailView.as_view()),
    path('mock/review-replies/', MockReviewReplyListView.as_view()),
    path('mock/review-replies/<int:pk>/', MockReviewReplyDetailView.as_view()),
]
