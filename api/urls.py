from django.urls import path
from .views import *

urlpatterns = [
    path('roles/', RoleListView.as_view()),
    path('roles/<int:pk>/', RoleDetailView.as_view()),
    path('access-rules/', AccessRoleListView.as_view()),
    path('access-rules/<int:pk>/', AccessRoleDetailView.as_view()),
]
