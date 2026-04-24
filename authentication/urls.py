from django.urls import path
from .views import RegisterView, LoginView, ProfileView, ProfileUpdateView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/update/', ProfileUpdateView.as_view()),
    path('logout/', LogoutView.as_view()),
]
