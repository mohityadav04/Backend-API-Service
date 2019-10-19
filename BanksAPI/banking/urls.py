from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', SignUpView.as_view()),
    path('branch-info/', BranchDetailView.as_view()),
    path('city-branches/', BankBranchesInCityView.as_view()),
]
